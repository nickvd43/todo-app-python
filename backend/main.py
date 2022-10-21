from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/check-status")
async def root():
    return {"Alive": True}

@app.post("/todo_item", response_model=schemas.TodoItemOut)
def create_todo_item(todo_item: schemas.TodoItemIn, db: Session = Depends(get_db)):
    print("hello")
    print(todo_item.task_description)
    return crud.create_todo_item(db, todo_item)

@app.get("/todo_item/{item_id}", response_model=schemas.TodoItemIn)
def get_todo_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_todo_item(db, item_id)

@app.get("/todo_items", response_model=list[schemas.TodoItemOut])
def get_todo_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("getting items")
    return crud.get_todo_items(db, skip, limit)

