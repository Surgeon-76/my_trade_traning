from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


user_name_db = 'name'
password_db = 'password'
db_name = 'my_shop_db'

engine = create_engine(
    f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}")

SessionLocal = sessionmaker(autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()
