from sqlalchemy.orm import Session

from app_shop.models import models
from app_shop.schemas import schemas


# Покупатели
# Ищем покупателя по id
def get_customer(db: Session, customer_id: int):
    return db.query(
        models.Customer).filter(models.Customer.id == customer_id).first()


# Ищем покупателя по email
def get_customer_by_email(db: Session, email: str):
    return db.query(
        models.Customer).filter(models.Customer.email == email).first()


# Выводим лимитированный список покупателей
def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


# Создание Покупателя
def create_customer(db: Session, customer: schemas.CustomerCreate):
    fake_hashed_password = customer.password + 'notreallyhashed'
    db_customer = models.Customer(
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


# Товар
# Выводим список товаров в заказе
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


# Создание товара
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        name=item.name,
        cost_price=item.cost_price,
        selling_price=item.selling_price,
        quantity=item.quantity
        )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# Заказы(дата)
# Выводим список заказов покупателя(-лей)
def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


# Создание заказа
def create_orders(db: Session, order: schemas.OrderCreate, customer_id: int):
    db_order = models.Order(**order.dict(), customer_id=customer_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


# Заказ - Товар(количество)
# Выводим список связей Заказ - Товаров
def get_order_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderItem).offset(skip).limit(limit).all()


# Создание связи Заказ - Товар
def create_order_items(db: Session, order_item: schemas.OrderItemCreate):
    db_order_items = models.OrderItem(**order_item.dict())
    # db_order_items = models.OrderItem(order_id=order_item.order_id, \
    #     item_id=order_item.item_id, quantity=order_item.quantity)
    db.add(db_order_items)
    db.commit()
    db.refresh(db_order_items)
    return db_order_items
