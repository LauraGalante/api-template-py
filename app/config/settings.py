import os
import pathlib
import secrets
from typing import List, Any

from pydantic import AnyHttpUrl, EmailStr, validator, BaseModel

ROOT = pathlib.Path(__file__).resolve().parent.parent



class Settings(BaseModel):
    APP_NAME: str



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

    @validator("SERVER", pre=True)
    def environment_server_url(cls, v, values):
        if "ENV" in values and values["ENV"] == "development":
            return [{"url": "https://staging.coinnodes.tech/sucn", "description": "Staging environment"}]
        elif "ENV" in values and values["ENV"] == "production":
            return [{"url": "https://production.coinnodes.tech/sucn", "description": "Production environment"}]
        return None


settings = Settings(**os.environ)