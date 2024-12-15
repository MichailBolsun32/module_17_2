from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models.products import Product

from app.backend import *



class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {'keep_existing': True}  # для создания дополнительных параметров в  таблицах
    # в нашем примере скорее всего для управления миграциями
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True) # может и не быть связей

    products = relationship("Product", back_populates="category") # связали 'Category' с 'Product'

from sqlalchemy.schema import CreateTable
print(CreateTable(Product.__table__))
print(CreateTable(Category.__table__))

