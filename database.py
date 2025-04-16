import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Get DATABASE_URL from environment variables (using the **variable name**)
database_url = os.environ.get("DATABASE_URL")

# Check if it's None and raise an error to help with debugging
if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set!")

# Connect to PostgreSQL
engine = create_engine(database_url, echo=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
