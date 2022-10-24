from sqlalchemy.orm import Session
from datetime import datetime as dt

from . import models, schemas

def get_todo_item(db: Session, item_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.item_id == item_id).first()

def get_todo_items(db:Session, skip: int, limit: int):
    return db.query(models.TodoItem).offset(skip).limit(limit).all()

def get_todo_items_by_completion_status(db: Session, status: bool, skip: int, limit: int):
    return db.query(models.TodoItem).offset(skip).limit(limit).filter(models.TodoItem.done == status).all()

def create_todo_item(db: Session, todo_item: schemas.TodoItemIn):
    db_todo_item = models.TodoItem(task_description=todo_item.task_description,
                                   datetime_added=dt.utcnow(),
                                   datetime_completed=None,
                                   done=False)
    db.add(db_todo_item)
    db.commit()
    db.refresh(db_todo_item)


    return db_todo_item

def update_todo_item_description(db: Session, updated_description: str, todo_item: schemas.TodoItemOut):
    todo_item.task_description = updated_description
    db.commit()
    db.refresh(todo_item)

    return todo_item


def update_todo_item_status(db: Session, todo_item: schemas.TodoItemOut):
    if not todo_item.done:
        todo_item.done = True
        todo_item.datetime_completed = dt.utcnow()
    else:
        todo_item.done = False
        todo_item.datetime_completed = None

    db.commit()
    db.refresh(todo_item)

    return todo_item

def remove_todo_item(db: Session, todo_item: schemas.TodoItemOut):
    db.delete(todo_item)
    db.commit()

