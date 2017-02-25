# -*- coding: utf-8 -*-

"""Database manager."""
from os.path import join

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.functions import (drop_database, database_exists,
                                        create_database)

from settings import APP_DATA

SQLITEDB_PATH = join(APP_DATA, "test.db")


def db_connect(path=SQLITEDB_PATH, echo=False):
    """Creates an SQLite DB and engine for daily dumps."""
    connection_string = "sqlite:///%s" % path

    return create_engine(connection_string, echo=echo, convert_unicode=True)


engine = db_connect()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db(engine=engine):
    """Create tables."""
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import workload.models
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)
    Base.metadata.create_all(bind=engine)
