FROM python:3.9

WORKDIR /app/

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3
ENV PATH="/opt/poetry/bin:$PATH"
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./app/poetry.lock* /app/

ARG INSTALL_DEV=true

ENV PYTHONPATH=/app

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY . /app

RUN chmod +x run.sh

CMD ["./run.sh"]