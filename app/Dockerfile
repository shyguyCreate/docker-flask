# syntax=docker/dockerfile:1

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim-bookworm

EXPOSE 8080

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Copy all files to /app directory
WORKDIR /app
COPY . .

# Install pip requirements
RUN python -m pip install -r requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["waitress-serve", "--port", "8080", "app:app"]
