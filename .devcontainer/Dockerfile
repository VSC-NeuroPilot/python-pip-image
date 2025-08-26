FROM python:3.13.6-slim-bullseye

# Build args (defaults for local builds)
ARG GITHUB_REPOSITORY=""
ARG APP_DIR="/workspace"
ENV APP_DIR=${APP_DIR}

LABEL org.opencontainers.image.source="https://github.com/${GITHUB_REPOSITORY}"
LABEL org.opencontainers.image.description="A Python container to use with NeuroPilot."
LABEL org.opencontainers.image.licenses="MIT"

# Create a dedicated 'python' user & group early so --chown=python:python works
# Use system user so it has a predictable uid/gid
RUN groupadd --system python \
 && useradd --system --create-home --gid python --shell /bin/bash python

# Install OS packages (do not install python3 — base image already has Python)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      ca-certificates curl build-essential git \
 && rm -rf /var/lib/apt/lists/*

# set absolute workdir
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

# Copy only requirements first (cache-friendly)
COPY requirements.txt ${APP_DIR}/

# Install Python deps as root (cached when requirements.txt unchanged)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the repo into the image and set ownership to the python user.
# NOTE: --chown requires BuildKit. If your environment doesn't support it, remove --chown and
# rely on the chown step below (which is tolerant).
COPY --chown=python:python . ${APP_DIR}

# Ensure permissions (tolerant). This avoids build failure on filesystems that disallow chown.
RUN if [ -d "${APP_DIR}" ]; then chown -R python:python "${APP_DIR}" || true; fi

# Switch to the non-root 'python' user
USER python
ENV HOME=/home/python

# Default command
CMD ["bash"]
