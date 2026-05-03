from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Base

db_url = "postgresql://postgres:malar@localhost:5432/api"

engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def start_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()