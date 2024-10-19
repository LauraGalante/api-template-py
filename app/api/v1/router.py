from fastapi import APIRouter, FastAPI


from app.api.v1.endpoint import root, oauth

api_router = APIRouter()
app = FastAPI()


api_router.include_router(root.router, tags=["root"])
api_router.include_router(oauth.router, tags=["oauth"])