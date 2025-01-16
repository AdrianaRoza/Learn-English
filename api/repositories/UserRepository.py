from api.database import db
from api.models.UserModel import User
from api.schemas.UserSchema import UserCreate
from sqlalchemy.future import select


# C CREATE
async def create(request_body: UserCreate):
    new_user = User(
        email=request_body.email, 
        name=request_body.name,
        password=request_body.password,
        is_active=True
        
    )
    db.add(new_user)
    await db.commit()
    db.refresh(new_user)
    return new_user

# R READ
async def get_all():
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()
   

# U UPDATE
async def update(user_id: int, request_body: UserCreate):
    query = await db.get(User, user_id)
    if not query:
        return {"message": "User not found"}
    else:
        query.name = request_body.name
        query.email = request_body.email
        query.password = request_body.password
        await db.commit()
        return query

# D DELETE
async def delete(user_id: int):
    user = await db.get(User, user_id)
    if not user:
        return {"message": "User not found"}
    await db.delete(user)
    await db.commit()
    return {"message": "User deleted successfully"}
