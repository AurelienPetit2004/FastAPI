from fastapi import FastAPI
import TodoApp.models as models
from TodoApp.database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
