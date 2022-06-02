# pull python image as base compile
FROM python:3.9 as requirements-stage

# set up the tem director
WORKDIR /tmp

# poetry setup and install
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/

# export requirements with poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# deploy stage
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# environment setup from build stage
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

# make sure we use the virtualenv:
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copy app directory
COPY . /app
