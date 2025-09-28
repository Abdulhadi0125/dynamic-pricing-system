# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY ./app/requirements.txt /app/

# Install system deps (needed for streamlit, supervisord logs, etc.)
RUN apt-get update && apt-get install -y \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and model folders
COPY ./app /app
COPY ./model /app/model

# Create logs folder
RUN mkdir -p /app/logs

# Copy supervisord config
COPY supervisord.conf /etc/supervisord.conf

# Expose FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# Start both processes using supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
