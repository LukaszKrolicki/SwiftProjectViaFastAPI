import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from config import engine, Base
from database import get_db
from models.swift_code import SwiftCode
from routes.swift_code_routes import router
from services.swift_code_load_service import load_swift_codes_from_csv
from config import csv_file_path

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = next(get_db())

    if not db.query(SwiftCode).first():
        load_swift_codes_from_csv(db, csv_file_path)
    yield
app = FastAPI(lifespan=lifespan)

Base.metadata.create_all(bind=engine)
app.include_router(router)
