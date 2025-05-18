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

## License

This project is open source and available under the MIT license.
