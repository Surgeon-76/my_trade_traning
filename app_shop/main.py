from fastapi import FastAPI

from .models import models
from .database.database import engine

from app_shop.routers import (
    customers,
    items,
    orderitems,
    orders
)


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(customers.customers_route)
app.include_router(orders.order_route)
app.include_router(items.items_route)
app.include_router(orderitems.links_route)
