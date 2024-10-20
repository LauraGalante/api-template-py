
<p align="center">
  <a href="https://coinnodes.tech/">
    <img src="https://www.coinnodes.tech/images/logo.png" alt="Logo da Coinnodes.tech" width="400"/>
  </a>
</p>

# Acesse nosso site: [coinnodes.tech](https://coinnodes.tech/)

**CoinNodes.tech:** *Trabalhamos no fornecimento de dados e tecnologia para o mercado de financeiro de bancos, pagamentos e criptoativos, proporcionando soluções avançadas e confiáveis para todos os envolvidos no setor, incluindo investidores, empresas e desenvolvedores.*

Para mais informações, visite nosso site [aqui](https://coinnodes.tech/en).

---

# Overview do Repositório - API em Python com FastAPI

Este repositório contém um exemplo de template de uma API desenvolvida em Python utilizando **FastAPI**. Abaixo, estão detalhadas as principais dependências e tecnologias utilizadas, bem como instruções de configuração com **Poetry**, gerenciamento de banco de dados com **Alembic**, tipagem de dados com **Pydantic**, e conteinerização da aplicação com **Docker**.

## Dependências e Gerenciamento de Pacotes com Poetry

Para facilitar o gerenciamento de dependências e versões, utilizamos o **Poetry**. Ele nos permite controlar facilmente as bibliotecas utilizadas na aplicação, garantindo versões compatíveis e segurança no ambiente de desenvolvimento.

### Instalação do Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Instalar Dependências

Após configurar o Poetry, as dependências do projeto podem ser instaladas com o comando:

```bash
poetry install
```

## API com FastAPI

**FastAPI** é um framework web moderno, rápido (alta performance) e fácil de usar, especialmente adequado para criar APIs RESTful. Ele utiliza Python tipo hints para validações automáticas de dados e gera documentação automática, como o **Swagger UI**.

### Benefícios do FastAPI

- Fácil de usar e intuitivo;
- Validações automáticas com base nas anotações de tipo do Python;
- Suporte para assíncronismo com asyncio;
- Geração automática de documentação via **OpenAPI** (Swagger).

### Instalação com Poetry

Para instalar o FastAPI, execute o comando:

```bash
poetry add fastapi
poetry add uvicorn[standard]  # Servidor para rodar a aplicação
```

### Rodar a aplicação FastAPI

Para iniciar o servidor FastAPI com Uvicorn:

```bash
poetry run uvicorn main:app --reload
```

A documentação da API estará disponível em: `http://127.0.0.1:8000/docs`

## Alembic para Versionamento de Banco de Dados

**Alembic** é uma ferramenta para gerenciamento de versões de banco de dados. Ele permite criar e aplicar migrações de maneira segura e organizada.

### Instalação com Poetry

Para instalar o Alembic:

```bash
poetry add alembic
```

### Configurar Alembic

Para inicializar o Alembic no projeto:

```bash
poetry run alembic init migrations
```

### Criar uma migração

```bash
poetry run alembic revision --autogenerate -m "descricao_da_migracao"
```

### Aplicar uma migração

```bash
poetry run alembic upgrade head
```

## Pydantic e Tipagem Estruturada

**Pydantic** é usado para garantir uma tipagem forte e validação de dados, através da criação de **DTOs (Data Transfer Objects)** e **modelos de resposta**.

### Benefícios de Pydantic

- Garantia de validação e tipagem de dados;
- Estruturação clara de objetos para entrada e saída de dados;
- Integração fácil com FastAPI.

### Instalação com Poetry

Para instalar o Pydantic:

```bash
poetry add pydantic
```

Exemplo de uso com DTOs no FastAPI:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

## SQLAlchemy para Gerenciamento de Banco de Dados

**SQLAlchemy** é uma biblioteca que fornece uma camada ORM para interação com o banco de dados utilizando objetos Python. Ele é frequentemente utilizado em conjunto com **Pydantic** para mapeamento de dados entre o banco e a aplicação.

### Instalação com Poetry

Para instalar o SQLAlchemy:

```bash
poetry add sqlalchemy
```

### Exemplo básico de uso:

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

# Configurar o engine e a sessão
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
```

## Containers e Docker

A aplicação é conteinerizada utilizando **Docker** para garantir que o ambiente seja replicável e portável. Utilizamos um **Dockerfile** para construir a imagem da aplicação e um **docker-compose.yaml** para configurar e rodar o ambiente completo.

### Dockerfile

O Dockerfile descreve como a imagem Docker é construída:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install --no-root

COPY . /app

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### docker-compose.yaml

O arquivo `docker-compose.yaml` facilita a execução de vários serviços em contêineres, como o banco de dados e a aplicação FastAPI:

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

### Comandos Básicos do Docker

- Para construir e rodar os contêineres:

```bash
docker compose up -d --build
```

- Para parar os contêineres:

```bash
docker compose down
```

---

© 2024 Coin Nodes LTDA. Todos os direitos reservados.

O código e a documentação escritos pertencem e foram construídos pela Coin Nodes LTDA. Estes possuem propriedade intelectual e estão protegidos pelas leis de copyright. Qualquer uso não autorizado, reprodução ou distribuição sem o consentimento explícito da Coin Nodes LTDA é estritamente proibido.
