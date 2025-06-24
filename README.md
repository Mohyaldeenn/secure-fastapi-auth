# Secure User Authentication API with FastAPI

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlalchemy)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

A professional, secure, and production-ready RESTful API service for user authentication and management. Built with modern Python technologies, this project demonstrates best practices in API development, including JWT-based security, password hashing, asynchronous database operations, and dependency injection.

## ✨ Key Features

- **Secure User Registration:** Endpoint to create new users with validated email and hashed passwords.
- **JWT Authentication:** OAuth2-compatible token endpoint (`/login/token`) for secure user login.
- **Password Security:** Uses `bcrypt` for hashing passwords. No plain text passwords are ever stored.
- **Protected Endpoints:** A clear example of how to protect routes, accessible only with a valid JWT.
- **Asynchronous Support:** Fully asynchronous from the API layer down to the database using `async/await`, `FastAPI`, and `SQLAlchemy 2.0`.
- **Database Migrations:** Uses `Alembic` to manage database schema changes reliably.
- **Dependency Injection:** Leverages FastAPI's dependency injection system for clean, reusable, and testable code (e.g., `get_db`, `get_current_user`).
- **Auto-generated Documentation:** Interactive API documentation available at `/docs` (Swagger UI) and `/redoc`.
- **Configuration Management:** Securely manages settings and secrets using `.env` files.

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL (with `asyncpg` driver)
- **ORM:** SQLAlchemy (with async support)
- **Database Migrations:** Alembic
- **Data Validation:** Pydantic
- **Security:** Passlib (for hashing), python-jose (for JWT)
- **Server:** Uvicorn

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.10+
- PostgreSQL Database Server
- Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mohyaldeenn/secure-fastapi-auth.git
    cd secure-fastapi-auth
    ```

2.  **Create and activate a virtual environment:**
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    - Create a `.env` file in the root directory by copying the example file:
      ```bash
      cp .env.example .env
      ```
    - Open the `.env` file and update the `DATABASE_URL` with your PostgreSQL credentials. You should also replace `SECRET_KEY` with a new securely generated key.
      ```
      # .env
      DATABASE_URL="postgresql+asyncpg://YOUR_POSTGRES_USER:YOUR_POSTGRES_PASSWORD@localhost:5432/fastapi_db"
      SECRET_KEY="a_new_super_secret_key_generated_with_openssl"
      ALGORITHM="HS256"
      ACCESS_TOKEN_EXPIRE_MINUTES=30
      ```

5.  **Apply database migrations:**
    - Make sure your PostgreSQL server is running and you have created the database specified in `DATABASE_URL`.
    - Run the following command to apply all migrations and create the necessary tables:
      ```bash
      alembic upgrade head
      ```

### Running the Application

Once the setup is complete, you can run the application with Uvicorn:

```bash
uvicorn app.main:app --reload
```
The API will be available at **`http://127.0.0.1:8000`**

## 📚 API Documentation

Once the application is running, you can access the interactive API documentation (powered by Swagger UI) at:

**`http://127.0.0.1:8000/docs`**

An alternative documentation (powered by ReDoc) is also available at:

**`http://127.0.0.1:8000/redoc`**

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.