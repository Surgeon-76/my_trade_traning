from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, \
    Numeric, DateTime, SmallInteger
from sqlalchemy.orm import relationship

from app_shop.database.database import Base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True, index=True)
    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    username = Column(String(50), nullable=False, index=True)
    email = Column(String(200), nullable=False, index=True)
    hashed_password = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now, index=True)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer())


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True, index=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now, index=True)
    line_items = relationship("OrderItem", backref='order')


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer(), primary_key=True, index=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")