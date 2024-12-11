from sqlalchemy import create_engine
from backend.db import Base, engine

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

# Проверка SQL-запросов
print(str(engine).replace("sqlite://", "SQLite - "))