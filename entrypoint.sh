python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn car_exchange.wsgi:application --bind 0.0.0.0:8000
