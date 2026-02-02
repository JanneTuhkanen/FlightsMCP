# Use Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_VERSION=1.0.0 \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

# Set working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Switch to non-root user
USER appuser

# Copy dependency files
COPY --chown=appuser:appuser pyproject.toml requirements.txt ./

# Create virtual environment and install dependencies
RUN uv venv && \
    uv pip install -r requirements.txt && \
    uv pip install -e .

# Copy application code
COPY --chown=appuser:appuser settings.py ./
COPY --chown=appuser:appuser app/ ./app/

# Expose port (adjust if your app uses a different port)
EXPOSE 8000

# Run the FastMCP server with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
