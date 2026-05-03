from database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

class product(Base):
    __tablename__="product"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float)
    count: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(255), nullable=False, server_default="")
    
    