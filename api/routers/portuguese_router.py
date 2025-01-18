from fastapi import APIRouter, HTTPException
from api.repositories import PortugueseRepository
from api.schemas.PortugueseSchema import PortugueseCreate, PortugueseResponse

router = APIRouter(
    prefix="/portuguese",
    tags=["Portuguese"],
)

# CREATE
@router.post("/", response_model=PortugueseResponse)
async def create_portuguese(request_body: PortugueseCreate):
    return await PortugueseRepository.create(request_body)

# READ
@router.get("/", response_model=list[PortugueseResponse])
async def get_all_portuguese():
    return await PortugueseRepository.get_all()

# UPDATE
@router.put("/{portuguese_id}", response_model=PortugueseResponse | dict)
async def update_portuguese(portuguese_id: int, request_body: PortugueseCreate):
    return await PortugueseRepository.update(portuguese_id, request_body)

# DELETE
@router.delete("/{portuguese_id}")
async def delete_portuguese(portuguese_id: int):
    return await PortugueseRepository.delete(portuguese_id)