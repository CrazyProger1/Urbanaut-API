FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /urbanaut
WORKDIR /urbanaut

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

RUN pip install --upgrade pip \
    && pip install poetry

COPY pyproject.toml /urbanaut/

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /urbanaut/

EXPOSE 8001

RUN chmod +x /urbanaut/entrypoint.sh

ENTRYPOINT ["/urbanaut/entrypoint.sh"]
