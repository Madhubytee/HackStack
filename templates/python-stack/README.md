# React + Python Flask + PostgreSQL Template

A fullstack application with Python backend and React frontend.

## Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Axios** - HTTP client for API calls
- Runs on port **3000**

### Backend
- **Python 3.11** - Programming language
- **Flask** - Lightweight web framework
- **psycopg2** - PostgreSQL adapter for Python
- **Flask-CORS** - Cross-origin resource sharing
- Runs on port **8000**

### Database
- **PostgreSQL 15** - Relational database
- Automatically creates tables on startup
- Persistent data storage with Docker volumes

## What's Included

- Health check endpoint
- CRUD operations for items
- Database connection with psycopg2
- Hot reload for development
- Dockerized environment

## API Endpoints

- `GET /api/health` - Check if backend is running
- `GET /api/items` - Get all items
- `POST /api/items` - Create a new item (send `{ "name": "item name" }`)

## Environment

All services run in isolated Docker containers and communicate through a Docker network.
