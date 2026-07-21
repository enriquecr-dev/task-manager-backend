from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Hardcoded for now. In production, we will move this to environment variables in the 'core' folder.
DATABASE_URL = "postgresql+psycopg://admin:admin_password@localhost:5432/task_manager"

# The engine is the core interface to the database
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal will be used to create independent database sessions for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class for all our SQLAlchemy models
class Base(DeclarativeBase):
    pass
