from api.database import db
from api.models.PortugueseModel import Portuguese
from api.schemas.PortugueseSchema import PortugueseCreate
from sqlalchemy.future import select


# C CREATE
async def create(request_body: PortugueseCreate):
    new_portuguese = Portuguese(word=request_body.word)
    db.add(new_portuguese)
    await db.commit()
    db.refresh(new_portuguese)
    return new_portuguese

# R READ
async def get_all():
    query = select(Portuguese)
    result = await db.execute(query)
    return result.scalars().all()
   

# U UPDATE
async def update(portuguese_id: int, request_body: PortugueseCreate):
    query = await db.get(Portuguese, portuguese_id)
    if not query:
        return {"message": "Word Portuguese not found"}
    else:
        query.word = request_body.word
        await db.commit()
        return query

# D DELETE
async def delete(portuguese_id: int):
    portuguese = await db.get(Portuguese, portuguese_id)
    if not portuguese:
        return {"message": "Word Portuguese not found"}
    await db.delete(portuguese)
    await db.commit()
    return {"message": "Word deleted successfully"}
