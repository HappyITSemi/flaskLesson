from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from setting import Base


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(24))
    due = Column(DateTime, nullable=False)


class Todo(Base):
    __tablename__ = 'todo'
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(24), nullable=False)
    description = Column(String(128), nullable=False)
    due_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    category_id = Column(Integer)
    # category_id = Column(Integer, ForeignKey('category.id'))
    # category = relationship('Category', backref='todo', uselist=False)
