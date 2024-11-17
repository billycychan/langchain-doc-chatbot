# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Specify Python version for the base image
ARG PYTHON_VERSION=3.12.6
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files and disables stdout/stderr buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Create a non-privileged user to run the application
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copy Pipfile and Pipfile.lock for dependency management
COPY Pipfile Pipfile.lock ./

# Install pipenv and project dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install pipenv && \
    pipenv install --deploy --system

# Switch to the non-privileged user
USER appuser

# Copy the source code into the container
COPY . .

# Expose the port the application listens on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "main.py"]
