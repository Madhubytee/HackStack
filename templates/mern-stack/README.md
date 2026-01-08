# MERN Stack Template

A complete MERN (MongoDB, Express, React, Node.js) application template.

## Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Axios** - HTTP client for API calls
- Runs on port **3000**

### Backend
- **Node.js** - JavaScript runtime
- **Express** - Web framework
- **Mongoose** - MongoDB object modeling
- **CORS** enabled
- Runs on port **8000**

### Database
- **MongoDB 7** - NoSQL document database
- Automatic collection creation
- Persistent data storage with Docker volumes

## What's Included

- Health check endpoint
- CRUD operations for documents
- MongoDB connection with Mongoose
- Hot reload for development
- Dockerized environment

## API Endpoints

- `GET /api/health` - Check if backend is running
- `GET /api/items` - Get all items
- `POST /api/items` - Create a new item (send `{ "name": "item name" }`)
- `DELETE /api/items/:id` - Delete an item

## Environment

All services run in isolated Docker containers and communicate through a Docker network.
