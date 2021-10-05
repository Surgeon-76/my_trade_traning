from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app_shop.crud import crud
from app_shop.schemas import schemas
from app_shop.dependcies.dependency import get_db


items_route = APIRouter(
    prefix="/items",
    tags=["Товары:"]
)


# Товары
# Создание товара
@items_route.post("/", summary=('Новый товар'), response_model=schemas.Item)
def create_items(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


# Просмотр товара
@items_route.get("/", summary=('Вывести список товаров'),
                 response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
