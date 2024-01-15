# Start with an Ubuntu base image
FROM ubuntu:latest

# Install Python, pip, and necessary libraries
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    poppler-utils \
    tesseract-ocr

# Alias python and pip to python3 and pip3
RUN ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

WORKDIR /app
COPY treatment_evaluation/docker /app/treatment_evaluation/docker

# Install Python dependencies
RUN --mount=type=cache,target=/root/.cache/pip pip install -r treatment_evaluation/docker/requirements.txt

# Copy your application code to the container
COPY . .

ENV PYTHONPATH /app

# Expose port for the application
EXPOSE 8080

# Command to run the application
CMD exec uvicorn treatment_evaluation.service:app --host 0.0.0.0 --port 8080
