from sqlalchemy import Column, String, Integer
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    userId = Column(String(12),unique=True)
    nickName = Column(String(25),unique=True)
    email = Column(String(100),unique=True,index=True)
    password = Column(String(30))