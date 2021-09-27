from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel,Field
from sqlalchemy.sql.sqltypes import DateTime



########################################## Товар
class ItemBase(BaseModel):
    name: str
    cost_price: float
    selling_price: float
    quantity: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int


    class Config:
        orm_mode = True


########################################### Заказ - Товар(кол-во)
class OrderItemBase(BaseModel):
    order_id: int
    item_id: int
    quantity: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int
    # order_id: int
    # item_id: int
    item: Item


    class Config:
        orm_mode = True


########################################### Заказы(дата)
class OrderBase(BaseModel):
    date_placed: datetime


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    customer_id: int
    line_items: List[OrderItem] = []


    class Config:
        orm_mode = True



########################################## Покупатели
class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str


class CustomerCreate(CustomerBase):
    password: str = Field(..., min_length=8, max_length=50)


class Customer(CustomerBase):
    id: int
    created_on: datetime
    updated_on: datetime

    orders: List[Order] = []


    class Config:
        orm_mode = True