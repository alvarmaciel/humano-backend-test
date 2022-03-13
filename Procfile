web: gunicorn humanoBackendTest.wsgi --log-file -
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
release:  python manage.py loaddata fixture_producto.json
release:  python manage.py loaddata fixture_socie.json