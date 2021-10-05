from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
)

from app_shop.database.database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer())
