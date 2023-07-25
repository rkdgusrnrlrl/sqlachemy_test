from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker

from models import Product


def test_autocommit_without_commit(session_factory: sessionmaker, auto_session_factory: sessionmaker):
    with session_factory() as session:
        pp = Product(id=1, name="상품01")
        session.add(pp)
        session.commit()

    with auto_session_factory() as auto_session:
        product: Product = auto_session.scalar(select(Product).where(Product.id == 1))
        product.name = "상품02"

    with auto_session_factory() as auto_session:
        product: Product = auto_session.scalar(select(Product).where(Product.id == 1))
        assert product.name == "상품01"


def test_autocommit_with_commit(session_factory: sessionmaker, auto_session_factory: sessionmaker):
    with session_factory() as session:
        pp = Product(id=1, name="상품01")
        session.add(pp)
        session.commit()

    with auto_session_factory() as auto_session:
        product: Product = auto_session.scalar(select(Product).where(Product.id == 1))
        product.name = "상품02"
        auto_session.commit()

    with auto_session_factory() as auto_session:
        product: Product = auto_session.scalar(select(Product).where(Product.id == 1))
        assert product.name == "상품02"


def test_autocommit_with_raw_query(session_factory: sessionmaker, auto_session_factory: sessionmaker):
    with session_factory() as session:
        pp = Product(id=1, name="상품01")
        session.add(pp)
        session.commit()

    with auto_session_factory() as auto_session:
        update_statm = update(Product).where(Product.id == 1).values(name="상품02")
        auto_session.execute(update_statm)

    with auto_session_factory() as auto_session:
        product: Product = auto_session.scalar(select(Product).where(Product.id == 1))
        assert product.name == "상품02"
