#!/usr/bin/env python3
import os
import sys
import shutil

def create_project(template_name, project_name):
    print(f"Creating {project_name} from {template_name} template...")

    # Check if template exists
    template_path = f"templates/{template_name}"
    if not os.path.exists(template_path):
        print(f"ERROR: Template '{template_name}' not found!")
        return

    #Check if project already exists
    if os.path.exists(project_name):
        print(f"ERROR: Folder '{project_name}' already exists!")
        return

    print(f"Copying template files...")
    shutil.copytree(template_path, project_name)

    os.chdir(project_name)

    #Starts the Docker containers
    print(f"Starting Docker containers...")
    print(f"   (This may take a few minutes the first time...)")
    os.system("docker-compose up -d --build")

    print(f"\nSuccess! Your project is ready!\n")
    print(f"Project: {project_name}")
    print(f"Frontend: http://localhost:3000")
    print(f"Backend:  http://localhost:8000")
    print(f"\nTo stop: cd {project_name} && docker-compose down")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python hackstack.py create <template> <project-name>")
        print("\nAvailable templates:")
        print("  - fullstack-app")
        sys.exit(1)

    command= sys.argv[1]
    template= sys.argv[2]
    project = sys.argv[3]

    if command == 'create':
        create_project(template, project)
    else:
        print(f"Unknown command: {command}")
