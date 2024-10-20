import os
import pathlib
import secrets
from typing import List, Any

from pydantic import AnyHttpUrl, EmailStr, validator, BaseModel

ROOT = pathlib.Path(__file__).resolve().parent.parent



class Settings(BaseModel):
    APP_NAME: str
    ENV: str 
    ROOT_PATH: str
    API_V1_STR: str
    API_V1_INT: int 
    DOCS_URL: str 
    REDOCS_URL: str
    DATABASE_URI: str


    @validator("DOCS_URL", pre=True)
    def environment_docs_url(cls, v, values):
        if "ENV" in values and values["ENV"] == "production":
            return None
        return v

    @validator("REDOCS_URL", pre=True)
    def environment_redocs_url(cls, v, values):
        if "ENV" in values and values["ENV"] == "production":
            return None
        return v

    # @validator("SERVER", pre=True)
    # def environment_server_url(cls, v, values):
    #     if "ENV" in values and values["ENV"] == "local":
    #         return [{"url": "https://staging.coinnodes.tech/sucn", "description": "Staging environment"}]
    #     elif "ENV" in values and values["ENV"] == "production":
    #         return [{"url": "https://production.coinnodes.tech/sucn", "description": "Production environment"}]
    #     return None


settings = Settings(**os.environ)