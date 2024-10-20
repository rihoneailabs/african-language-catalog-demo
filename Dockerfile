FROM python:3.12-slim AS builder


WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.12-slim AS runtime

# We need the odbc drivers at runtime
# https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16
# first install curl
RUN apt-get update && apt-get install -y curl &&  apt-get install -y gpg
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN apt-get purge -y curl gpg

RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*
COPY . .

# Change ownership of the app folder
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

# Default command for running the Flask app
CMD ["gunicorn", "--workers", "1", "application:app"]
