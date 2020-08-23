from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


Base = declarative_base()


class TodoCategory(Base):
    __tablename__ = 'todo_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(24))
    due = Column(DateTime, nullable=False)


class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(24), nullable=False)
    description = Column(String(128), nullable=False)
    due_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

