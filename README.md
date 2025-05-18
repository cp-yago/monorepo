# Monorepo Project

A simple and elegant monorepo containing a React frontend with Vite and a Python backend with FastAPI.

## Project Structure

```
monorepo/
├── apps/
│   ├── frontend/       # React with Vite
│   └── backend/        # Python with FastAPI
├── docker-compose.yml
└── README.md
```

## Technologies

- **Frontend**: React 18, TypeScript, Vite 5
- **Backend**: Python 3.12, FastAPI 0.109.2
- **Containerization**: Docker, Docker Compose

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Project

1. Clone the repository
2. Run the following command at the root of the project:

```bash
docker compose up
```

3. Access the applications:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Development

### Frontend

The frontend is a React application built with Vite. It includes:

- TypeScript support
- Hot module replacement for development
- Axios for API requests

### Backend

The backend is a FastAPI application. It includes:

- RESTful API endpoints
- CORS middleware configured for the frontend
- Interactive API documentation with Swagger UI

#### Installing Backend Dependencies

To add a new dependency to the backend:

1. Enter the virtual environment:

   ```bash
   cd apps/backend
   source venv/bin/activate
   ```

2. Install the new dependency:

   ```bash
   pip install dependency==x.y.z
   ```

3. Add the dependency to requirements.txt:

   ```bash
   pip freeze | grep dependency >> requirements.txt
   ```

4. When done, exit the virtual environment:
   ```bash
   deactivate
   ```

## License

This project is open source and available under the MIT license.
