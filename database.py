from sqlalchemy.orm import sessionmaker

import config
from config import *

DATABASE_URL = config.DATABASE_URL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=config.engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()