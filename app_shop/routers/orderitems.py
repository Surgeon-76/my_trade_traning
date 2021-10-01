from typing import List

from sqlalchemy.orm import Session
from fastapi import (
    APIRouter,
    Depends
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
