from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
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
