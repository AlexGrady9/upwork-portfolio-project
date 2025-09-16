# FastAPI User CRUD Example

This project is a minimal REST API for user management built with FastAPI, SQLAlchemy, and Pydantic. It is perfect for portfolio demonstration, test tasks, or as a quickstart template for new projects.

## 🚀 Features
- Register, view, update, and delete users
- SQLite database (easily replaceable)
- Asynchronous endpoints
- Tests with pytest + httpx

## 📦 Tech Stack
- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic (migrations)
- Pytest, httpx (testing)

## ⚡ Quickstart

1. Clone the repository:
   ```bash
   git clone https://github.com/AlexGrady9/upwork-portfolio-project.git
   cd upwork-portfolio-project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy the example environment variables:
   ```bash
   cp .env.example .env
   ```
   (or create .env manually using the example)
4. Run the application:
   ```bash
   python run.py
   ```
   The app will be available at http://127.0.0.1:8000

## 🧪 Running Tests

```powershell
# On Windows, run tests from the project root like this:
$env:PYTHONPATH = "src"
pytest
```

## 🛠️ Example .env
```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
```

## 📚 API Examples

- Get all users:
  ```http
  GET /api/v1/users
  ```
- Create a user:
  ```http
  POST /api/v1/users
  Content-Type: application/json
  {
    "email": "user@example.com",
    "name": "John Doe"
  }
  ```

## 📝 Contacts

Author: Alexey Gradinar
GitHub: [AlexGrady9](https://github.com/AlexGrady9)

---

> This project was created to demonstrate Python backend skills. Feel free to reach out with any questions!
