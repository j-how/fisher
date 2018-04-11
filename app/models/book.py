from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    author = Column(String(30), default='未名')
    isbn = Column(String(15), unique=True)
    price = Column(DECIMAL(8, 2))
    binding = Column(String(20))
    publisher = Column(String(50))
    pages = Column(Integer)
    summary = Column(String(1000))
    image = Column(String(50))
    pubdate = Column(DateTime, default=datetime.now())
