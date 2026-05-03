from fastapi import FastAPI
from sqlalchemy import create_engine
from database_models import Table,Base
from schemas import validate
import ingest 

app = FastAPI()
app.include_router(ingest.router)

db_url="postgresql://postgres:malar@localhost:5432/api"
engine=create_engine(db_url)
Base.metadata.create_all(bind=engine)
