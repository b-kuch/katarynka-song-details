FROM python:3.11 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

#CMD ["uvicorn", "src.streaming.main:app", "--host", "0.0.0.0", "--port", "8081"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
 CMD ["uvicorn", "src.details.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]