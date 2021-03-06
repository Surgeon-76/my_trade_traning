from fastapi import FastAPI

from app_shop.database.database import (
    Base,
    engine
)
from app_shop.routers import (
    customers,
    items,
    orderitems,
    orders
)


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Супер-пупер МеГаШоП",
    description="Первый блин всегда комом)))"
)

app.include_router(customers.customers_route)
app.include_router(orders.order_route)
app.include_router(items.items_route)
app.include_router(orderitems.links_route)
