from pydantic import BaseModel
from typing import Union

class PortugueseBase(BaseModel):
    word: str

class PortugueseCreate(PortugueseBase):
    pass

class PortugueseResponse(PortugueseBase):
    id: int

    class Config:
        orm_mode = True
