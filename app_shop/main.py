from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .crud import crud
from .models import models
from .schemas import schemas
from .database.database import SessionLocal, engine
from .dependcies.dependency import get_db

from app_shop.routers import customers
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(customers.customers_route)
# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# ############################################################## Покупатели
# # Создание нового
# @app.post("/customers/", response_model=schemas.Customer)
# def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
#     db_customer = crud.get_customer_by_email(db, email=customer.email)
#     if db_customer:
#         raise HTTPException(status_code=400, detail="Email уже зарегестрирован")
#     return crud.create_customer(db=db, customer=customer)

# # Посмотр лимитированного списка 
# @app.get("/customers/", response_model=List[schemas.Customer])
# def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     customers = crud.get_customers(db, skip=skip, limit=limit)
#     return customers

# # Поиск по ID
# @app.get("/customers/{customer_id}", response_model=schemas.Customer )
# def read_customer(customer_id: int, db: Session = Depends(get_db)):
#     db_customer = crud.get_customer(db, customer_id=customer_id)
#     if db_customer is None:
#         raise HTTPException(status_code=404, detail="Такого покупателя нет!")
#     return db_customer

############################################################## Дата заказа
# Создание нового заказа
@app.post("/customers/{customer_id}/orders/", response_model=schemas.Order)
def create_order_for_customaser(customer_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_orders(db=db, order=order, customer_id=customer_id)

# Просмотр даты заказа
@app.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

############################################################## Товары
# Создание товара
@app.post("/items/", response_model=schemas.Item)
def create_items(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# Просмотр товара
@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


############################################################## связь Заказ -Товар
# Создание связи
@app.post("/links/", response_model=schemas.OrderItem)
def create_links(links: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_order_items(db=db, order_item=links)
    
# Просмотр связи
@app.get("/links/", response_model=List[schemas.OrderItem])
def read_links(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    order_items = crud.get_order_items(db, skip=skip, limit=limit)
    return order_items