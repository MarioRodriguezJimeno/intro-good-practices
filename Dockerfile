FROM python:3.14
 
WORKDIR /code
 
COPY pyproject.toml poetry.lock* /code/
 
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root
 
COPY ./src /code/src
 
CMD ["fastapi", "run", "src/main.py", "--port", "80"]