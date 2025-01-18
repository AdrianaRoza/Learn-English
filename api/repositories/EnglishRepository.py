from api.database import db
from api.models.EnglishModel import English
from api.schemas.EnglishSchema import EnglishCreate
from sqlalchemy.future import select


# C CREATE
async def create(request_body: EnglishCreate):
    new_english = English(word=request_body.word)
    db.add(new_english)
    await db.commit()
    db.refresh(new_english)
    return new_english

# R READ
async def get_all():
    query = select(English)
    result = await db.execute(query)
    return result.scalars().all()
   

# U UPDATE
async def update(english_id: int, request_body: EnglishCreate):
    query = await db.get(English, english_id)
    if not query:
        return {"message": "Word English not found"}
    else:
        query.word = request_body.word
        await db.commit()
        return query

# D DELETE
async def delete(english_id: int):
    english = await db.get(English, english_id)
    if not english:
        return {"message": "Word English not found"}
    await db.delete(english)
    await db.commit()
    return {"message": "Word deleted successfully"}
