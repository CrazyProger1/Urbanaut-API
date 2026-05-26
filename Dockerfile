# pull official base image
FROM python:3.14-slim-bookworm

  # set work directory
WORKDIR /urbanaut

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        gdal-bin libgdal-dev \
        binutils libproj-dev \
        make curl zstd && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | sh

  # set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
UV_LINK_MODE=copy \
UV_PYTHON_DOWNLOADS=never \
UV_PROJECT_ENVIRONMENT=/urbanaut/.pyenv

  # install uv
COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uvx /bin/

  # Since there's no point in shipping lock files, we move them
  # into a directory that is NOT copied into the runtime image.
  # The trailing slash makes COPY create `/_lock/` automagically.
COPY pyproject.toml uv.lock /_lock/

  # Synchronize dependencies.
  # This layer is cached until uv.lock or pyproject.toml change.
RUN --mount=type=cache,target=/root/.cache \
cd /_lock && \
uv sync \
--frozen \
--no-install-project

  # copy project
COPY . .

RUN chmod +x /urbanaut/entrypoint.sh
ENTRYPOINT ["/urbanaut/entrypoint.sh"]