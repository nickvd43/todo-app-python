from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class TodoItem(Base):
    __tablename__ = "todo_items"

    task_description = Column(String)
    datetime_added = Column(DateTime)
    datetime_completed = Column(DateTime)
    done = Column(Boolean)
    item_id = Column(Integer, primary_key=True, index=True)