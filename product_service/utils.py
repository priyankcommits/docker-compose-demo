import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from connection import engine, session_scope


Base = declarative_base()


class Product(Base):
    __tablename__ = 'PRODUCTS'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    price = sqlalchemy.Column(sqlalchemy.String(100))
    quantity = sqlalchemy.Column(sqlalchemy.Integer)


def load_initial_data():
    Base.metadata.create_all(engine)
    products = [
        {'name': 'iPhone XS', 'price': '1000', 'quantity': 100},
        {'name': 'iPhone X', 'price': '700', 'quantity': 50},
        {'name': 'iPhone SE', 'price': '400', 'quantity': 10},
    ]
    with session_scope() as session:
        for product in products:
            session.add(Product(**product))
        session.commit()
    return
