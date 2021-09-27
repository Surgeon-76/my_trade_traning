from typing import List
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from app_shop.crud import crud
from app_shop.schemas import schemas
from app_shop.dependcies.dependency import get_db

customers_route = APIRouter(
    prefix="/customers",
    tags=['Покупатели:']
)

############################################################## Покупатели
# Создание нового

# @app.post("/customers/", response_model=schemas.Customer)
@customers_route.post("/", tags=['Создать'], response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db, email=customer.email)
    if db_customer:
        raise HTTPException(status_code=400, detail="Email уже зарегестрирован")
    return crud.create_customer(db=db, customer=customer)


# Посмотр лимитированного списка 
#@app.get("/customers/", response_model=List[schemas.Customer])
@customers_route.get("/", tags=['Показать всех'], response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers

# Поиск по ID
#@app.get("/customers/{customer_id}", response_model=schemas.Customer )
@customers_route.get("/{customer_id}", tags=['Показать одного'], response_model=schemas.Customer )
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Такого покупателя нет!")
    return db_customer
