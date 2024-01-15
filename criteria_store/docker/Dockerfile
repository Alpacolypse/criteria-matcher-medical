FROM python:3.10-slim

WORKDIR /app
COPY criteria_store/docker /app/criteria_store/docker

# Install Python dependencies
RUN --mount=type=cache,target=/root/.cache/pip pip install -r /app/criteria_store/docker/requirements.txt

# Copy your application code to the container
COPY . .

ENV PYTHONPATH /app

# Expose port for the application
EXPOSE 8000

# Command to run the application
CMD exec uvicorn criteria_store.service:app --host 0.0.0.0 --port 8000