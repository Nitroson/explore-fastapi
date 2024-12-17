# FastAPI Tutorial Project

This repository contains a comprehensive tutorial on **FastAPI**, a modern, fast, and high-performance web framework for Python.

The tutorial covers essential FastAPI concepts and step-by-step implementation for building APIs and web applications.

---

## Topics Covered

1. **Introduction to FastAPI**
   - Overview of FastAPI and its benefits.

2. **Path Parameters**
   - Handling dynamic routes using path parameters.

3. **Query Parameters**
   - Managing additional data in requests using query parameters.

4. **FastAPI Documentation**
   - Exploring interactive documentation (Swagger UI & ReDoc).

5. **Event Handlers**
   - Using event handlers to manage application startup and shutdown.

6. **CRUD Operations**
   - Implementing Create, Read, Update, and Delete operations.

7. **Pydantic**
   - Data validation and serialization using Pydantic models.

8. **Building a Simple App**
   - Integrating all concepts into a functional FastAPI application.

9. **Templates and Static Files**
   - Serving HTML templates and static files (CSS, JS, images).

---

## Project Structure

```
fastapi-tutorial/
└── app/
    └── main.py        # Main FastAPI application
    └── models.py      # Pydantic models
    └── routes.py      # API route definitions
    └── templates/    # HTML templates
    └── static/       # Static files (CSS, JS, images)
└── requirements.txt  # List of dependencies
└── README.md         # Project documentation
```

---

## Requirements

- **Python 3.8+**
- **FastAPI**
- **Uvicorn** (ASGI server for FastAPI)
- **Pydantic**

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Project

To run the FastAPI application:

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd fastapi-tutorial
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Open your browser and navigate to:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Key Features

- **Interactive API Documentation**
- **Dynamic Path and Query Parameters**
- **Event Handling**
- **CRUD Operations**
- **Data Validation with Pydantic**
- **Serving Templates and Static Files**

---


Happy Coding! 🚀
