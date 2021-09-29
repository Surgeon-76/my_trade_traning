from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app_shop.dependcies.dependency import get_db
from app_shop.crud import crud
from app_shop.schemas import schemas


order_route = APIRouter(
    prefix='/orders',
    tags=['Заказы']
)

# Дата заказа
# Создание нового заказа


@order_route.post("/customers/{customer_id}/", summary=('Создать заказ'), response_model=schemas.Order)
def create_order_for_customaser(customer_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_orders(db=db, order=order, customer_id=customer_id)

# Просмотр даты заказа


@order_route.get("/", summary=('Показать заказы'), response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders