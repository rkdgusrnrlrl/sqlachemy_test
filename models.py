from __future__ import annotations

from typing import List

from sqlalchemy import ForeignKey, Table, Column, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


association_table = Table(
    "association_table",
    Base.metadata,
    Column("prod_id", ForeignKey("product.id")),
    Column("cate_id", ForeignKey("category.id")),
)


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    products: Mapped[List[Product]] = relationship(
        secondary=association_table,
        cascade="all, delete"
    )

