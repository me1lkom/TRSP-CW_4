from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Product
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Product(title="Товар 1", price=100, count=5),
    Product(title="Товар 2", price=200, count=10)
])
session.commit()