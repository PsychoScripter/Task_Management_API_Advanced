# Task Management API Advanced

## Overview
Task Management API Advanced is a robust and scalable RESTful API designed to help users efficiently manage tasks and projects. It provides a comprehensive set of features including task creation, updating, deletion, user authentication, and role-based access control. This API is built with best practices in mind, aiming to deliver high performance, security, and ease of integration.

## Features
- User registration and authentication (JWT-based)
- Role-based access control (Admin, User roles)
- CRUD operations for tasks and projects
- Advanced filtering and sorting options for tasks
- Pagination support for large datasets
- Detailed error handling and validation
- Secure password hashing and token management
- API documentation with example requests and responses

## Technologies Used
- Python
- Django / Django REST Framework
- JWT Authentication
- PostgreSQL (or another database)
- Docker (if applicable)
- Dependencies listed in `requirements.txt`




## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- PostgreSQL (or your preferred database)
- Git
- Docker and Docker Compose (optional, for containerized deployment)

### Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/PsychoScripter/Task_Management_API_Advanced.git
   cd Task_Management_API_Advanced


2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables (database credentials, secret keys, etc.):

   ```bash
   cp .env.example .env
   ```
5. Run migrations:

   ```bash
   python manage.py migrate
   ```
6. (Optional) Create a superuser/admin account:

   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:

   ```bash
   python manage.py runserver
   ```

### Running with Docker

You can run the project using Docker in two ways:

#### 1. Using Docker CLI

Build the Docker image:

```bash
docker build -t task-management-api .
```

Run the container:

```bash
docker run -d -p 8000:8000 --env-file .env task-management-api
```

#### 2. Using Docker Compose

If your project includes a `docker-compose.yml` file, simply run:

```bash
docker-compose up -d
```

This will start all services defined in the Compose file, including the API and database, making setup much easier.

---
