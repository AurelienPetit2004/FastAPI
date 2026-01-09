from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQL_ALCHEMY_DATABASE_URL = "sqlite:///./TodoApp/todos.db"

engine = create_engine(url=SQL_ALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

sessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)

Base = declarative_base()
