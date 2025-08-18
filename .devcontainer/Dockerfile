FROM python:3.13.6-slim-bullseye

# Build args (defaults for local builds)
ARG GITHUB_REPOSITORY=""
ARG APP_DIR="/workspace"
ENV APP_DIR=${APP_DIR}

LABEL org.opencontainers.image.source="https://github.com/${GITHUB_REPOSITORY}"
LABEL org.opencontainers.image.description="A Python container to use with NeuroPilot."
LABEL org.opencontainers.image.licenses="MIT"

# Install OS packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl build-essential git python3 \
  && rm -rf /var/lib/apt/lists/*

# set absolute workdir
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

# Copy package manifests first (cache-friendly)
COPY requirements.txt ${APP_DIR}/

# Copy rest of the repo (this includes .vscode if you want it in the image)
COPY --chown=python:python . ${APP_DIR}

RUN pip install -r requirements.txt

# Ensure permissions (tolerant)
RUN if [ -d "${APP_DIR}" ]; then chown -R node:node "${APP_DIR}" || true; fi

USER python
ENV HOME=/home/python
