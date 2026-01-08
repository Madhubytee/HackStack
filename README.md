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

# Create a project
python hackstack.py create fullstack-app my-project

# Open browser
# Frontend: http://localhost:3000
# Backend:  http://localhost:8000
```

## Available Templates

- `fullstack-app` - React + Node.js + PostgreSQL

## Stop Containers

```bash
cd my-project
docker-compose down
```
