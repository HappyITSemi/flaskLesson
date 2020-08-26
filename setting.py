import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

SECRET_KEY = os.environ.get('SECRET_KEY')
STRIPE_API_KEY = ''

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

POSTGRESQL_DATABASE = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'admin',
    'password': 'password',
    'host': '127.0.0.1',
    'name': 'pg_db'
})
MYSQL_DATABASE = 'mysql+pymysql://{user}:{password}@{host}/{name}'.format(**{
    'user': 'admin',
    'password': 'password',
    'host': 'localhost',
    'name': 'mysql_db'
})
ENGINE = create_engine(
    POSTGRESQL_DATABASE,
    encoding="utf-8",
    echo=True)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()
# if Not Table create_table
# Base.metadata.create_all(ENGINE)

