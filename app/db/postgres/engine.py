from sqlalchemy import event, create_engine
from sqlmodel import Session

from app.config.settings import settings


def set_search_path(connection, record):
    with connection.begin():
        connection.execute("SET search_path TO public;")
        connection.execute("SET TIME ZONE 'America/Sao_Paulo'")


engine = create_engine(settings.DATABASE_URI, echo=True)
event.listen(engine, 'engine_connect', set_search_path)


def get_postgres():
    with Session(engine) as session:
        yield session