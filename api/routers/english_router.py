from fastapi import APIRouter, HTTPException
from api.repositories import EnglishRepository
from api.schemas.EnglishSchema import EnglishCreate, EnglishResponse

router = APIRouter(
    prefix="/english",
    tags=["English"],
)

# CREATE
@router.post("/", response_model=EnglishResponse)
async def create_english(request_body: EnglishCreate):
    return await EnglishRepository.create(request_body)

# READ
@router.get("/", response_model=list[EnglishResponse])
async def get_all_english():
    return await EnglishRepository.get_all()

# UPDATE
@router.put("/{english_id}", response_model=EnglishResponse | dict)
async def update_english(english_id: int, request_body: EnglishCreate):
    return await EnglishRepository.update(english_id, request_body)

# DELETE
@router.delete("/{english_id}")
async def delete_english(english_id: int):
    return await EnglishRepository.delete(english_id)
    