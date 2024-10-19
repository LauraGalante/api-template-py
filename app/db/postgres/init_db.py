import json
import logging
import random
import time
from pathlib import Path

from passlib.context import CryptContext
from sqlmodel import SQLModel, Session, select

from app.config.settings import settings
from app.core.entity import User, Role, MFA, CurrencyType, Currency, EmailTemplate, PaymentMethod, Services, Provider
from app.core.entity.role import RoleLevelType
from app.db.postgres.engine import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
