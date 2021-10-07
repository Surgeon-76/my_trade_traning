from typing import List

from sqlalchemy.orm import Session
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from app_shop.crud import crud
from app_shop.schemas import schemas
from app_shop.dependcies.dependency import get_db


links_route = APIRouter(
    prefix="/links",
    tags=['Связь:']
)


# связь Заказ -Товар
# Создание связи
@links_route.post("/", summary=('Создать связь'),
                  response_model=schemas.OrderItem)
def create_links(links: schemas.OrderItemCreate,
                 db: Session = Depends(get_db)):
    return crud.create_order_items(db=db, order_item=links)


# Просмотр связи
@links_route.get("/", summary=('Показать связи'),
                 response_model=List[schemas.OrderItem])
def read_links(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    order_items = crud.get_order_items(db, skip=skip, limit=limit)
    return order_items


# Редактирование связи
@links_route.put("/{order_items_id}",
                 summary=('Редактирование схемы заказа(изменение заказчика \
                     либо товара'),
                 response_model=schemas.OrderItemBase)
def edit_order_items(order_items_id: int,
                     order_item: schemas.OrderItemBase,
                     db: Session = Depends(get_db)):
    db_order_item = crud.update_order_items(
        db=db, order_items_id=order_items_id, order_item=order_item)
    if db_order_item is None:
        raise HTTPException(
            status_code=404,
            detail="Такой схемы заказа нет! Изменение невозможно!")
    return db_order_item
