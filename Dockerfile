# /home/siisi/portfolio/Dockerfile

# 1. Base image
FROM python:3.12.0

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Create work directory
WORKDIR /app

# 4. Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev netcat-openbsd gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copy project code
COPY . .

# 7. Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 8. Default command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
