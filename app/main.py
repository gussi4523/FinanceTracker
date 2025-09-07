from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

if __name__ == "__main__":
    # Create tables in FinanceTrackerDB (if they don’t exist yet)
    models.Base.metadata.create_all(bind=engine)
