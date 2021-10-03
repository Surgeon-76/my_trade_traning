from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    DateTime,
)
from sqlalchemy.orm import relationship

from app_shop.database.database import Base


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True, index=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now, index=True)
    line_items = relationship("OrderItem", backref='order')
