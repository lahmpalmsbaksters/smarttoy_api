from fastapi import APIRouter

router = APIRouter()


@router.get('/healthcheck')
async def healthcheck():
    try:
        message_healthcheck = 'healthcheck successfully'
        return {"message": message_healthcheck}
    except Exception as e:
        return e
