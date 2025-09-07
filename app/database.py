from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#URL
DATABASE_URL = "postgresql+psycopg2://finance:222password@localhost:5432/FinanceTrackerDB"

#DB engine inisialize
engine = create_engine(DATABASE_URL)
#DB Session inisialize
Session = sessionmaker(autocommit=False, autoflush=False,bind=engine)
#Base for models
Base = declarative_base()

try:
    with engine.connect() as conn:
        print("PostgreSQL connection OK ✅")
except Exception as e:
    print("Connection failed ❌", e)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()