from sqlalchemy.orm import Session
from fastapi import HTTPException

from app_shop.models import (
    customer_model,
    item_model,
    order_model,
    orderitem_model
)
from app_shop.schemas import schemas


# Покупатели
# Ищем покупателя по id
def get_customer(db: Session, customer_id: int):
    return db.query(
        customer_model.Customer).filter(
            customer_model.Customer.id == customer_id).first()


# Ищем покупателя по email
def get_customer_by_email(db: Session, email: str):
    return db.query(
        customer_model.Customer).filter(
            customer_model.Customer.email == email).first()


# Выводим лимитированный список покупателей
def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(customer_model.Customer).offset(skip).limit(limit).all()


# Создание Покупателя
def create_customer(db: Session, customer: schemas.CustomerCreate):
    fake_hashed_password = customer.password + 'notreallyhashed'
    db_customer = customer_model.Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        username=customer.username,
        email=customer.email,
        hashed_password=fake_hashed_password
        )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


# Редактирование Покупателя
def update_customer(db: Session,
                    customer_id: int, customer: schemas.CustomerBase):
    customer = {key: value for key, value in customer.dict().items()
                if value != 'string'}
    if not len(customer):
        raise HTTPException(
            status_code=400,
            detail="Должно быть изменено хоть одно из полей!!!")
    db.query(customer_model.Customer).filter(
        customer_model.Customer.id == customer_id).update(
            customer, synchronize_session='fetch')
    db.commit()
    return db.query(customer_model.Customer).filter(
        customer_model.Customer.id == customer_id).first()


# Товар
# Выводим список товаров в заказе
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item_model.Item).offset(skip).limit(limit).all()


# Создание товара
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = item_model.Item(
        name=item.name,
        cost_price=item.cost_price,
        selling_price=item.selling_price,
        quantity=item.quantity
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Редактирование товара
def update_item(db: Session, item_id: int, item: schemas.ItemBase):
    item = {key: value for key, value in item.dict().items()
            if value != 'string' and value != 0}
    if not len(item):
        raise HTTPException(
            status_code=400,
            detail="Должно быть изменено хоть одно из полей!!!")
    db.query(item_model.Item).filter(
        item_model.Item.id == item_id).update(
        item, synchronize_session='fetch')
    db.commit()
    return db.query(item_model.Item).filter(
        item_model.Item.id == item_id).first()


# Заказы(дата)
# Выводим список заказов покупателя(-лей)
def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(order_model.Order).offset(skip).limit(limit).all()


# Создание заказа
def create_orders(db: Session, order: schemas.OrderCreate, customer_id: int):
    db_order = order_model.Order(**order.dict(), customer_id=customer_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


# Редактирование заказа(изменение заказчика)
def update_orders(db: Session, order: schemas.OrderUpdate, order_id: int):
    order = {key: value for key, value in order.dict().items()
             if value != 0}
    if not len(order):
        raise HTTPException(
            status_code=400,
            detail="Должно быть изменено хоть одно из полей!!!")
    db.query(order_model.Order).filter(
        order_model.Order.id == order_id).update(
        order, synchronize_session='fetch')
    db.commit()
    return db.query(order_model.Order).filter(
        order_model.Order.id == order_id).first()


# Заказ - Товар(количество)
# Выводим список связей Заказ - Товаров
def get_order_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(orderitem_model.OrderItem).offset(skip).limit(limit).all()


# Создание связи Заказ - Товар
def create_order_items(db: Session, order_item: schemas.OrderItemCreate):
    db_order_items = orderitem_model.OrderItem(**order_item.dict())
    db.add(db_order_items)
    db.commit()
    db.refresh(db_order_items)
    return db_order_items


# Изменение связи(заказчика либо заказа)
def update_order_items(db: Session,
                       order_items_id: int,
                       order_item: schemas.OrderItemUpdate):
    order_item = {key: value for key, value in order_item.dict().items()
                  if value != 0}
    print(order_item)
    if not len(order_item):
        raise HTTPException(
            status_code=400,
            detail="Должно быть изменено хоть одно из полей!!!")
    db.query(orderitem_model.OrderItem).filter(
        orderitem_model.OrderItem.id == order_items_id).update(
        order_item, synchronize_session='fetch')
    db.commit()
    return db.query(orderitem_model.OrderItem).filter(
        orderitem_model.OrderItem.id == order_items_id).first()


# Удаление связи
def del_order_items(db: Session, order_items_id: int):
    db_order_items = db.query(orderitem_model.OrderItem).filter(
        orderitem_model.OrderItem.id == order_items_id).one_or_none()
    if not db_order_items:
        return None
    db.delete(db_order_items)
    db.commit()
    return db_order_items
