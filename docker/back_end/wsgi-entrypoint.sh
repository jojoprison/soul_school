#!/bin/sh

until cd /app/back_end/back_end/
do
    echo "Waiting for back_end volume..."
done
cd ..

# Apply database migrations
#python manage.py migrate
#python /app/back_end/manage.py migrate
#./manage.py migrate

# Collect static files
#./manage.py collectstatic --noinput
#python /app/back_end/manage.py collectstatic --noinput

# Start the WSGI server
gunicorn back_end.wsgi:application --bind 0.0.0.0:8000
echo "start"
