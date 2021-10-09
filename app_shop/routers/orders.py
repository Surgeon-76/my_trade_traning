from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app_shop.dependcies.dependency import get_db
from app_shop.crud import crud
from app_shop.schemas import schemas


order_route = APIRouter(
    prefix='/orders',
    tags=['Заказы:']
)


# Дата заказа
# Создание нового заказа
@order_route.post("/customers/{customer_id}", summary=('Создать заказ'),
                  response_model=schemas.Order)
def create_order_for_customer(customer_id: int, order: schemas.OrderCreate,
                              db: Session = Depends(get_db)):
    return crud.create_orders(db=db, order=order, customer_id=customer_id)


# Просмотр даты заказа
@order_route.get("/", summary=('Показать заказы'),
                 response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100,
                db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


# Редактирование заказа(изменение заказчика)
@order_route.put("/{order_id}",
                 summary=('Редактирование заказа(изменение заказчика)'),
                 response_model=schemas.OrderUpdate)
def edit_orders(order_id: int,
                order: schemas.OrderUpdate,
                db: Session = Depends(get_db)):
    db_order = crud.update_orders(db=db, order_id=order_id, order=order)
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Такого заказа нет! Редактирование невозможно!")
    return db_order


# Удаление заказа
@order_route.delete("/{order_id}",
                    summary=('Удаление схемы заказа'))
def del_order(order_id: int,
              db: Session = Depends(get_db)):
    db_order = crud.delete_orders(
        db=db, order_id=order_id)
    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Такого заказа нет! Удаление невозможно!"
        )
    return db_order
