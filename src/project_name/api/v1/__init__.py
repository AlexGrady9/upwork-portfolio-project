from fastapi import APIRouter
from .user import router as user_router

router = APIRouter()


@router.get("/test")
async def test():
    return {"message": "API v1 is working"}

router.include_router(user_router)
