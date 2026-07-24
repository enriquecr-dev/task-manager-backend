import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# 1. Añadimos la raíz del proyecto al path para poder importar nuestra Clean Architecture
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# 2. Importamos nuestra URL de base de datos y la clase Base
from src.infrastructure.database import DATABASE_URL, Base

# 3. CRÍTICO: Debemos importar TODOS nuestros modelos aquí para que Alembic los descubra
from src.infrastructure.models.user import User

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 4. Le pasamos los metadatos de SQLAlchemy a Alembic
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    configuration = config.get_section(config.config_ini_section, {})

    # 5. Sobrescribimos la URL dinámicamente con nuestra variable
    configuration["sqlalchemy.url"] = DATABASE_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
