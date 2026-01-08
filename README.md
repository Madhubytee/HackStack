# HackStack

Instant dev environments for hackathons.

## Requirements

- Docker Desktop (running)
- Python 3.7+

## Quick Start

```bash
# Clone this repo
git clone <your-repo-url>
cd hackstack

# Create a project with any template
python hackstack.py create fullstack-app my-project
# or
python hackstack.py create mern-stack my-project
# or
python hackstack.py create python-stack my-project

# Open browser
# Frontend: http://localhost:3000
# Backend:  http://localhost:8000
```

## Available Templates

### fullstack-app
**Stack:** React + Node.js + PostgreSQL
- Modern React frontend
- Express backend with REST API
- PostgreSQL relational database
- Perfect for: Traditional web apps, CRUD applications

### mern-stack
**Stack:** React + Node.js + MongoDB
- React frontend
- Express backend with Mongoose ODM
- MongoDB NoSQL database
- Perfect for: Real-time apps, flexible data models

### python-stack
**Stack:** React + Python Flask + PostgreSQL
- React frontend
- Python Flask backend
- PostgreSQL relational database
- Perfect for: Data science projects, ML integration

## Stop Containers

```bash
cd my-project
docker-compose down
```
