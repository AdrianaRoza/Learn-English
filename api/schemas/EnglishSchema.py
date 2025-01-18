from pydantic import BaseModel

class EnglishBase(BaseModel):
    word: str

class EnglishCreate(EnglishBase):
    pass

class EnglishResponse(EnglishBase):
    id: int

    class Config:
        orm_mode = True
