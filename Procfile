web: gunicorn humanoBackendTest.wsgi --log-file -
release: python manage.py makemigrations --noimput
release: python manage.py collectstatic --noimput
release: python manage.py migrate --noimput
