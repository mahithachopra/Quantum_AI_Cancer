# Base image
FROM python:3.13-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install system packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create runtime directories
RUN mkdir -p logs outputs

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI
# Start FastAPI
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]