from typing import List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
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


# Редактирование товара
@items_route.put("/{item_id}", summary=('Редактирование товара'),
                 response_model=schemas.Item)
def edit_items(item_id: int,
               item: schemas.ItemBase,
               db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if not db_item:
        raise HTTPException(
            status_code=404,
            detail="Такого товара нет! Редактирование невозможно!")
    return db_item


# Удаление товара
@items_route.delete("/{item_id}", summary=('Удаление товара'))
def del_items(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_items(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(
            status_code=404,
            detail="Такого товара нет! Удаление невозможно!"
        )
    return db_item
