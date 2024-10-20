from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=None)
async def root():
    return {"API Test-laula": "This is my test api. My husband obligate me to do this pls call 911."

            }