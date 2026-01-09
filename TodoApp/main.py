from typing import Annotated
import time
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import TodoApp.models as models
from TodoApp.database import engine, sessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(models.Todos).all()


@app.get("/test-thread-issue")
async def test_thread_issue(db: Annotated[Session, Depends(get_db)]):
    # Force the session to get a connection
    db.execute(text("SELECT 1"))
    
    # Now sleep (holds the connection)
    time.sleep(5)
    
    # Try to use it again
    return db.query(models.Todos).all()
