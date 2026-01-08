# React + Node.js + PostgreSQL Template

A fullstack application template with modern web technologies.

## Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Axios** - HTTP client for API calls
- Runs on port **3000**

### Backend
- **Node.js** - JavaScript runtime
- **Express** - Web framework
- **CORS** enabled for cross-origin requests
- Runs on port **8000**

### Database
- **PostgreSQL 15** - Relational database
- Automatically creates tables on startup
- Persistent data storage with Docker volumes

## What's Included

- Health check endpoint (`/api/health`)
- CRUD operations for items (`/api/items`)
- Database connection pooling
- Hot reload for development
- Dockerized environment

## API Endpoints

- `GET /api/health` - Check if backend is running
- `GET /api/items` - Get all items
- `POST /api/items` - Create a new item (send `{ "name": "item name" }`)

## Environment

All services run in isolated Docker containers and communicate through a Docker network.
