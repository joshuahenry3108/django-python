FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy everything (project will be generated into this folder shortly)
COPY . /code/

# Default dev command (migrate, then runserver)
CMD sh -c "python manage.py migrate && gunicorn myproject.wsgi:application --bind 0.0.0.0:8080"

