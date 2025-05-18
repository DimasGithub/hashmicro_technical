FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY db.sqlite3 .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "hashapp.wsgi:application", "--bind", "0.0.0.0:8080"]