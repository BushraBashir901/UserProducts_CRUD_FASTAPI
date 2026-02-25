FASTAPI CRUD OPERATIONS:
A simple FastAPI project demonstrating CRUD operations for users and products using SQLite and SQLAlchemy.

FEATURES:
1. Create, Read, Update, Delete (CRUD) for Users
2. Create, Read, Update, Delete (CRUD) for Products
3. SQLAlchemy ORM for database interactions
4. Pydantic models for request validation
5. Automatic API documentation with FastAPI `/docs`

INSTALLATION:
1. Clone the repository
-> git clone <https://github.com/BushraBashir901/UserProducts_CRUD_FASTAPI>

2. Change directory
-> cd user_products_crud_operations

3. Create virtual environment (optional)
->python -m venv envapi
.\envapi\Scripts\Activate.ps1  # Windows PowerShell

4. Install dependencies
  pip install fastapi
  pip install uvicorn
  pip install sqlalchemy
  pip install pydantic

5. Run
Run the server
-> uvicorn main:app --reload --port 5000

Visit Swagger docs
-> http://127.0.0.1:5000/docs

6. Usage
   Use /users endpoints to manage users
   Use /products endpoints to manage products
   All endpoints support CRUD operations
