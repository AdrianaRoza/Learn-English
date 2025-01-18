from sqlalchemy import  Column, Integer, String
from api.database import Base

class Portuguese (Base):
    __tablename__ = "portuguese"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, nullable=False)
    