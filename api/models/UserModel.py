from sqlalchemy import Boolean, Column, Integer, String
from api.database import Base

class User (Base):
    __tablename__ = "users2"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
