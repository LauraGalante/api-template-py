
<p align="center">
  <a href="https://coinnodes.tech/">
    <img src="https://www.coinnodes.tech/images/logo.png" alt="Coinnodes.tech Logo" width="400"/>
  </a>
</p>

# Visit our website: [coinnodes.tech](https://coinnodes.tech/)

**CoinNodes.tech:** *We work on providing data and technology for the financial market of banks, payments, and crypto-assets, offering advanced and reliable solutions for all involved in the sector, including investors, companies, and developers.*

For more information, visit our website [here](https://coinnodes.tech/en).

---

# Repository Overview - API with Python using FastAPI

This repository contains an example template of an API built with Python using **FastAPI**. Below, we detail the main dependencies and technologies used, as well as setup instructions with **Poetry**, database version control with **Alembic**, type-safe data handling with **Pydantic**, and application containerization with **Docker**.

## Dependencies and Package Management with Poetry

To facilitate dependency and version management, we use **Poetry**. It allows us to easily manage the libraries used in the application, ensuring compatible versions and security in the development environment.

### Poetry Installation

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Install Dependencies

After configuring Poetry, the project dependencies can be installed with the command:

```bash
poetry install
```

## API with FastAPI

**FastAPI** is a modern, fast (high-performance) web framework, easy to use, and particularly suited for building RESTful APIs. It uses Python type hints for automatic data validation and generates automatic documentation, such as **Swagger UI**.

### Benefits of FastAPI

- Easy to use and intuitive;
- Automatic validation based on Python type annotations;
- Asynchronous support with asyncio;
- Automatic documentation generation via **OpenAPI** (Swagger).

### Installation with Poetry

To install FastAPI, run the command:

```bash
poetry add fastapi
poetry add uvicorn[standard]  # Server to run the application
```

### Running the FastAPI Application

To start the FastAPI server with Uvicorn:

```bash
poetry run uvicorn main:app --reload
```

API documentation will be available at: `http://127.0.0.1:8000/docs`

## Alembic for Database Versioning

**Alembic** is a tool for database version control. It allows you to create and apply migrations in a safe and organized way.

### Installation with Poetry

To install Alembic:

```bash
poetry add alembic
```

### Configure Alembic

To initialize Alembic in the project:

```bash
poetry run alembic init migrations
```

### Create a Migration

```bash
poetry run alembic revision --autogenerate -m "migration_description"
```

### Apply a Migration

```bash
poetry run alembic upgrade head
```

## Pydantic for Structured Typing

**Pydantic** is used to ensure strong typing and data validation by creating **DTOs (Data Transfer Objects)** and **response models**.

### Benefits of Pydantic

- Guarantee of data validation and typing;
- Clear structuring of objects for input and output data;
- Easy integration with FastAPI.

### Installation with Poetry

To install Pydantic:

```bash
poetry add pydantic
```

Example of usage with DTOs in FastAPI:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

## SQLAlchemy for Database Management

**SQLAlchemy** is a library that provides an ORM layer for interacting with databases using Python objects. It is often used together with **Pydantic** for data mapping between the database and the application.

### Installation with Poetry

To install SQLAlchemy:

```bash
poetry add sqlalchemy
```

### Basic Usage Example:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Configure the engine and session
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
```

## Containers and Docker

The application is containerized using **Docker** to ensure that the environment is replicable and portable. We use a **Dockerfile** to build the application image and a **docker-compose.yaml** to configure and run the full environment.

### Dockerfile

The Dockerfile describes how the Docker image is built:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install --no-root

COPY . /app

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### docker-compose.yaml

The `docker-compose.yaml` file makes it easy to run multiple services in containers, such as the database and the FastAPI application:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DATABASE_URL=sqlite:///./test.db

  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: app_db
```

### Basic Docker Commands

- To build and run the containers:

```bash
docker compose up -d --build
```

- To stop the containers:

```bash
docker compose down
```

---

© 2024 Coin Nodes LTDA. All rights reserved.

The code and documentation written belong to and were created by Coin Nodes LTDA. They are intellectual property and are protected by copyright laws. Any unauthorized use, reproduction, or distribution without the explicit consent of Coin Nodes LTDA is strictly prohibited.
