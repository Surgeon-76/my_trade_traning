from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


user_name_db = 'surglin'
password_db = 'Nusha230399'
db_name = 'my_shop_db'

engine = create_engine(f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}")

SessionLocal = sessionmaker(autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()