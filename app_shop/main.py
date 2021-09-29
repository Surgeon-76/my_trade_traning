from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .crud import crud
from .models import models
from .schemas import schemas
from .database.database import SessionLocal, engine
from .dependcies.dependency import get_db

from app_shop.routers import customers, orders
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(customers.customers_route)
app.include_router(orders.order_route)


# Товары
# Создание товара


@app.post("/items/", response_model=schemas.Item)
def create_items(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# Просмотр товара


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


# связь Заказ -Товар
# Создание связи
@app.post("/links/", response_model=schemas.OrderItem)
def create_links(links: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_order_items(db=db, order_item=links)

# Просмотр связи


@app.get("/links/", response_model=List[schemas.OrderItem])
def read_links(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    order_items = crud.get_order_items(db, skip=skip, limit=limit)
    return order_items
