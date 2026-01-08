#!/usr/bin/env python3
import os
import sys
import shutil

def create_project(template_name, project_name):
    print(f"Creating {project_name} from {template_name} template...")

    # Get the directory where hackstack.py is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Check if template exists (relative to script location)
    template_path = os.path.join(script_dir, "templates", template_name)
    if not os.path.exists(template_path):
        print(f"ERROR: Template '{template_name}' not found!")
        return

    # Convert project_name to absolute path
    project_path = os.path.abspath(project_name)

    #Check if project already exists
    if os.path.exists(project_path):
        print(f"ERROR: Folder '{project_path}' already exists!")
        return

    print(f"Copying template files...")
    shutil.copytree(template_path, project_path)

    os.chdir(project_path)

    #Starts the Docker containers
    print(f"Starting Docker containers...")
    print(f"   (This may take a few minutes the first time...)")
    os.system("docker-compose up -d --build")

    print(f"\nSuccess! Your project is ready!\n")
    print(f"Project: {project_path}")
    print(f"Frontend: http://localhost:3000")
    print(f"Backend:  http://localhost:8000")
    print(f"\nTo stop: cd {project_path} && docker-compose down")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python hackstack.py create <template> <project-name>")
        print("\nAvailable templates:")
        print("  - fullstack-app   (React + Node.js + PostgreSQL)")
        print("  - mern-stack      (React + Node.js + MongoDB)")
        print("  - python-stack    (React + Python Flask + PostgreSQL)")
        sys.exit(1)

    command= sys.argv[1]
    template= sys.argv[2]
    project = sys.argv[3]

    if command == 'create':
        create_project(template, project)
    else:
        print(f"Unknown command: {command}")
