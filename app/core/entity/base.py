from datetime import datetime

import pytz
from sqlalchemy import Column, DateTime
from sqlmodel import SQLModel, Field


class Base(SQLModel):
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)),
                                 default=datetime.now(tz=pytz.timezone("America/Sao_Paulo")))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True)),
                                 default=datetime.now(tz=pytz.timezone("America/Sao_Paulo")))
    is_active: bool = Field(default=True)
