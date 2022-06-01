# pull python image as base compile
FROM python:3.10 as requirements-stage

# set up the tem director
WORKDIR /tmp

# poetry setup and install
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/

# export requirements with poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# pull the official docker image
FROM python:3.10

# set work directory
WORKDIR /app

# set env variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# environment setup from build stage
COPY --from=requirements-stage /tmp/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy project
COPY . .
