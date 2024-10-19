from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=None)
async def root():
    return {"API Coin Nodes Group": "More information dev@coinnodes.tech!",
            "API Version": "1.0.0",
            "API Documentation": "https://app.coinnodes.tech/",
            "API Status": "OK",
            "ROOT": "/docs"}