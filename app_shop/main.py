from fastapi import FastAPI

from .database.database import Base, engine
from app_shop.routers import (
    customers,
    items,
    orderitems,
    orders
)


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customers.customers_route)
app.include_router(orders.order_route)
app.include_router(items.items_route)
app.include_router(orderitems.links_route)
