{% if cookiecutter.use_docker == "yes" -%}
# Python {{ cookiecutter.python_version }}
FROM python:{{ cookiecutter.python_version }}-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml README.md ./
COPY src/ src/

# Install package
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

{% if cookiecutter.include_cli == "yes" -%}
# Set entrypoint
ENTRYPOINT ["{{ cookiecutter.project_slug }}"]
{% else -%}
# Run Python
CMD ["python"]
{% endif -%}
{% endif -%}
