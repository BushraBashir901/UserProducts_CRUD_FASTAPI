from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL
SQLALCHEMY_DB_URL = 'sqlite:///./sql_app.db'

# Engine
engine = create_engine(
    SQLALCHEMY_DB_URL,
    connect_args={"check_same_thread": False}  # only for SQLite
)

# SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

