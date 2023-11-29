# models.py
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, default=None)  # None으로 변경
    phone_number = Column(String, default=None)  # None으로 변경
    image_binary = Column(LargeBinary)

class UserTime(Base) :
    __tablename__ = "user_time"
    user_id = Column(Integer, ForeignKey("user_info.id"))
    id = Column(Integer, primary_key=True, index=True)  
    income_time = Column(DateTime, default=None)  
    outcome_time = Column(DateTime, default=None)  