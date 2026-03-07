from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    category_id = Column(Integer, ForeignKey("categories.id"))

    name = Column(String, nullable=False)
    description = Column(String)

    price = Column(Float)
    stock = Column(Integer)

    unit = Column(String)
    image_url = Column(String)