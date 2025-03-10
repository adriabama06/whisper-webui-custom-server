FROM python:3.10-slim-bullseye

# Install system dependencies and clean up in the same layer to reduce image size
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    libffi-dev \
    libssl-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

# Install runtime dependencies to reduce final image size
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && find /usr/local/lib/python3.10/site-packages -name "*.pyc" -delete \
    && find /usr/local/lib/python3.10/site-packages -name "__pycache__" -delete

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.enableCORS", "false", "--server.address=0.0.0.0", "--server.port=8501"]
