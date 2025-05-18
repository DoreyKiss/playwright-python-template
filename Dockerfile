# Base image with Playwright and Python
FROM mcr.microsoft.com/playwright/python:v1.51.0-noble

RUN pip install poetry 

WORKDIR /app

# Copy only the necessary files first to leverage Docker cache
COPY pyproject.toml poetry.lock* ./

# Install dependencies (will install virtualenv in .venv inside container)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Now copy the rest of the source code
COPY . .

RUN poetry run playwright install chromium firefox

# todo create a safer user for test run

CMD ["poetry", "run", "pytest", "--self-contained-html"]