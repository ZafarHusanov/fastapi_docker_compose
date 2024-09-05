from fastapi import APIRouter

router = APIRouter(
    prefix='',
    tags=[''],
    responses={404:{'description': 'Not found'}},
)

@router.get('/users')
async def read_users():
    return ["Zafar", "Ali"]