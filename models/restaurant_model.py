from sqlalchemy import Column, Integer, String
from database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    mobile = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String)
    password_hash = Column(String, nullable=False)
