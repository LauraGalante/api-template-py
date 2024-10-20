import logging
from fastapi import FastAPI
from fastapi.responses import FileResponse
from sqlmodel import Session
from starlette.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.config.settings import settings

favicon_path = 'static/logo.ico'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
# logger = logging.getLogger(_name_)

app = FastAPI(
    debug=True,
    servers=(
        [{"url": "https://staging.pixusglobal.com/otc", "description": "Staging environment"}]
        if settings.ENV == "staging"
        else [{"url": "https://production.pixusglobal.com/otc", "description": "Production environment"}]
        if settings.ENV == "production"
        else None
    ),
    root_path_in_servers=False,
    root_path=settings.ROOT_PATH,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOCS_URL,
    title=settings.APP_NAME,
    openapi_url="/api/v1/openapi.json",
    version=settings.API_V1_INT
)

# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_credentials=True,
#         allow_origins=["*"],
#         allow_methods=["*"],
#         allow_headers=["*"],
#         expose_headers=["*"]
#     )


# @app.on_event("startup")
# def on_startup():
#     logger.info("Starting up the application.")
#     if settings.ENV != "production":
#         try:
#             with Session(engine) as db:
#                 create_initial_data(db)
#         except Exception as e:
#             logger.error(f"Error during startup: {e}")
#             raise e
#     # Iniciar o scheduler
#     schedule_jobs()  # Isso inicia as duas tarefas
#     logger.info("Application startup complete.")


@app.get("", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


app.include_router(api_router, prefix=settings.API_V1_STR)