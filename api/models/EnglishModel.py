from sqlalchemy import  Column, Integer, String
from api.database import Base

class English (Base):
    __tablename__ = "english"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, nullable=False)
    