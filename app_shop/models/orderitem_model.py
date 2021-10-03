from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    SmallInteger
)
from sqlalchemy.orm import relationship

from app_shop.database.database import Base


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer(), primary_key=True, index=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")
