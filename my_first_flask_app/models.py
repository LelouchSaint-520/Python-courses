from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class Message(Base):
    __tablename__ = "messages"  # 告诉SQLAlchemy这个类对应数据库里的哪个表

    # 定义表的列
    id = Column(Integer, primary_key=True, index=True)
    visitor_name = Column(String, nullable=False)
    visitor_message = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
