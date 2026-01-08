# HackStack

Instant dev environments for hackathons (or any other project)! Save the hours of setup time so you can work on your idea right away. 

## Requirements

- Docker Desktop (running)
- Python 3.7+

## Quick Start

```bash
# 1. Clone this repo
git clone <your-repo-url>

# 2. Navigate to where you want your project created
cd path/to/your/projects/folder


# 3. Run HackStack with your chosen template (the path is where you downlaoded hackstack)
python path/to/hackstack.py create fullstack-app my-project

# Example: If HackStack is on your Desktop and you want the project in Documents
cd C:\Users\YourName\Documents
python C:\Users\YourName\Desktop\HackStack\hackstack.py create fullstack-app my-project

# 4. Open your browser
# Frontend: http://localhost:3000
# Backend:  http://localhost:8000
```

**How it works:**
- HackStack creates the project in whatever folder you're currently in (your `cd` location)
- You run the Python script from wherever HackStack is located
- Choose any template: `fullstack-app`, `mern-stack`, or `python-stack`

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
