from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool

from app.config.settings import settings
from app.core.entity.base import Base
# Replace this with the path to your database configuration or model definition
from app.db.postgres.engine import engine

config = context.config
# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Set the metadata for "api" schema
Base.metadata.schema = "api"
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=str(engine.url),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema="api"  # specify the schema for alembic version table
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        settings.DATABASE_URI,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema="api"  # specify the schema for alembic version table
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()