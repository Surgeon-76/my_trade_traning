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


customers_route = APIRouter(
    prefix="/customers",
    tags=['Покупатели:']
)


# Покупатели
# Создание нового
@customers_route.post("/", summary=('Создать'),
                      response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate,
                    db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db, email=customer.email)
    if db_customer:
        raise HTTPException(
            status_code=400, detail="Email уже зарегестрирован")
    return crud.create_customer(db=db, customer=customer)


# Посмотр лимитированного списка
@customers_route.get("/", summary=('Показать всех'),
                     response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100,
                   db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers


# Поиск по ID
@customers_route.get("/{customer_id}", summary=('Поиск покупателя по ID'),
                     response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Такого покупателя нет!")
    return db_customer


# Редактирование покупателя
@customers_route.put("/{customer_id}", summary=('Редактирование покупателя'),
                     response_model=schemas.Customer)
def edit_customers(customer_id: int,
                   customer: schemas.CustomerBase,
                   db: Session = Depends(get_db)):
    db_customer = crud.update_customer(
        db=db, customer_id=customer_id, customer=customer)
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Такого покупателя нет! Редактирование невозможно!")
    return db_customer


# Удаление покупателя
@customers_route.delete("/{customer_id}",
                        summary=('Удаление покупателя'))
def del_customer(customer_id: int,
                 db: Session = Depends(get_db)):
    db_customer = crud.delete_customer(
        db=db, customer_id=customer_id)
    if not db_customer:
        raise HTTPException(
            status_code=404,
            detail="Такого покупателя нет! Удаление невозможно!"
        )
    return db_customer
