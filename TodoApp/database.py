from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQL_ALCHEMY_DATABASE_URL = "sqlite:///./TodoApp/todos.db"

engine = create_engine(url=SQL_ALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(create_engine, autoflush=False, autocommit=False)

Base = declarative_base()
