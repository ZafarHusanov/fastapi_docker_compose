from fastapi import APIRouter

from src.endpoints.users import crud

router = APIRouter(prefix='/api')
router.include_router(crud.router)