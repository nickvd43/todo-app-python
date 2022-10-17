import datetime

from pydantic import BaseModel
from pydantic.schema import Optional

class TodoItemIn(BaseModel):
    task_description: str

    class Config:
        orm_mode = True

class TodoItemOut(BaseModel):
    item_id: int
    done: bool
    datetime_completed: Optional[datetime.datetime]
    datetime_added: datetime.datetime
    task_description: str

    class Config:
        orm_mode = True