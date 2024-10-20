FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.12-slim AS runtime

RUN useradd -m appuser
WORKDIR /app

# Install azure sql deps
RUN apt-get install unixodbc-dev && apt-get install msodbcsql18

# Copy Python dependencies from builder stage
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# Install dependencies from wheels
RUN pip install --no-cache /wheels/*

# Copy application code
COPY . .

# Change ownership of the application directory
RUN chown -R appuser:appuser /app
USER appuser

CMD ["gunicorn", "--workers", 1, "application:app"]  
