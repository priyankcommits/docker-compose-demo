import os
import sys
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = os.environ["PRODUCT_SERVICE_DB_HOST"]
DB_NAME = os.environ["PRODUCT_SERVICE_DB_NAME"]
DB_USER = os.environ["PRODUCT_SERVICE_DB_USER"]
DB_PASSWORD = os.environ["PRODUCT_SERVICE_DB_PASSWORD"]

connection_string = 'mysql://{}:{}@{}/{}'.format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

sys.stdout.write("Connecting to the database \n")
sys.stdout.flush()

engine = create_engine(connection_string, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def get_engine():
    return engine


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
