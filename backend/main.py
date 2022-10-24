from fastapi import Depends, FastAPI, HTTPException
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
    return crud.create_todo_item(db, todo_item)

@app.get("/todo_item/{item_id}", response_model=schemas.TodoItemOut)
def get_todo_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_todo_item(db, item_id)

@app.put("/todo_item/{item_id}/description", response_model=schemas.TodoItemOut)
def update_todo_item_description(item_id: int, todo_item: schemas.TodoItemIn, db: Session = Depends(get_db)):

    existing_item = crud.get_todo_item(db, item_id)
    if not existing_item:
        return HTTPException(404, "Given item id was not found")
    else:
        return crud.update_todo_item_description(db, todo_item.task_description, existing_item)

@app.put("/todo_item/{item_id}/status", response_model=schemas.TodoItemOut)
def update_todo_item_status(item_id: int, db: Session = Depends(get_db)):

    existing_item = crud.get_todo_item(db, item_id)
    if not existing_item:
        return HTTPException(404, "Given item id was not found")
    else:
        return crud.update_todo_item_status(db, existing_item)

@app.get("/todo_items", response_model=list[schemas.TodoItemOut])
def get_todo_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("getting items")
    return crud.get_todo_items(db, skip, limit)

@app.delete("/todo_item/{item_id}")
def get_todo_item(item_id: int, db: Session = Depends(get_db)):
    existing_item = crud.get_todo_item(db, item_id)
    if not existing_item:
        return HTTPException(404, "Given item id was not found")
    else:
        crud.remove_todo_item(db, existing_item)
        return {"OK" : f"Item with {item_id} was deleted"}
