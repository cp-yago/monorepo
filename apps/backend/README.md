# Backend API

This is the backend API for the application. It's built with FastAPI and SQLModel.

## Project Structure

```
apps/backend/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── users.py        # User endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py      # App configuration
│   │   └── database.py    # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py        # User database model
│   ├── repositories/      # NEW: Database interaction layer
│   │   ├── __init__.py
│   │   ├── base.py       # Base repository with common operations
│   │   └── user.py       # User-specific database operations
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py        # User request/response schemas
│   └── services/
│       ├── __init__.py
│       └── user.py        # User business logic
├── main.py                # Application entry point
├── requirements.txt       # Project dependencies
└── README.md             # This file

```

## Layer Responsibilities

- **models/**: Database models using SQLModel
- **schemas/**: Request/Response models using Pydantic
- **services/**: Business logic layer
- **repositories/**: Database interaction layer
- **api/**: API endpoints
- **core/**: Core configurations and utilities

## Adding a New Router

To add a new feature to the API, follow these steps:

1. Create the Model:

```python
# app/models/feature.py
from sqlmodel import SQLModel, Field

class Feature(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    # Add other fields
```

2. Create the Schemas:

```python
# app/schemas/feature.py
from pydantic import BaseModel

class FeatureBase(BaseModel):
    name: str

class FeatureCreate(FeatureBase):
    pass

class FeatureResponse(FeatureBase):
    id: int
```

3. Create the Repository:

```python
# app/repositories/feature.py
from app.repositories.base import BaseRepository
from app.models.feature import Feature

class FeatureRepository(BaseRepository[Feature]):
    def __init__(self, session):
        super().__init__(Feature, session)
```

4. Create the Service:

```python
# app/services/feature.py
from app.repositories.feature import FeatureRepository
from app.schemas.feature import FeatureCreate

class FeatureService:
    def __init__(self, session):
        self.repository = FeatureRepository(session)

    def create_feature(self, feature: FeatureCreate):
        return self.repository.create(feature.model_dump())
```

5. Create the Router:

```python
# app/api/features.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.services.feature import FeatureService
from app.schemas.feature import FeatureCreate, FeatureResponse

router = APIRouter()

@router.post("/features", response_model=FeatureResponse)
def create_feature(
    *,
    session: Session = Depends(get_session),
    feature: FeatureCreate
):
    service = FeatureService(session)
    return service.create_feature(feature)
```

6. Register the Router:

```python
# main.py
from app.api.features import router as features_router

# Add with other routers
app.include_router(features_router, prefix="/api", tags=["features"])
```

## Setup and Running

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn main:app --reload
```

## API Documentation

After running the application, visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
