#!/bin/bash

# Set the default values for some fields if not provided
if [ -z "$REDIS_PORT" ]; then
echo "entrypoint.sh: REDIS_PORT is unset, setting default (default = 6379)"
REDIS_PORT=6379
fi

if [ -z "$DB_NAME" ]; then
echo "entrypoint.sh: DB_NAME is unset, setting default (default = \"teamlock\")"
DB_NAME=teamlock
fi

if [ -z "$DB_PORT" ]; then
echo "entrypoint.sh: DB_PORT is unset, setting default (default = 5432)"
DB_PORT=5432
fi

if [ -z "$PUBLIC_URI" ]; then
echo "entrypoint.sh: PUBLIC_URI is unset, setting default (default = \"\/\")"
PUBLIC_URI="\/"
fi

# Alter Postgresql,Redis & Public URI informations in the settings.py
# CAUTION: the "/" must be escaped in the environment variable
cat Teamlock/settings.py \
| sed -e "s/REDIS_HOST = \"<REDIS_HOST>\"/REDIS_HOST = \"$REDIS_HOST\"/g" \
| sed -e "s/REDIS_PORT = 6379/REDIS_PORT = $REDIS_PORT/g" \
| sed -e "s/'NAME': '<DB_NAME>',/'NAME': '$DB_NAME',/g" \
| sed -e "s/'HOST': '<DB_IP>',/'HOST': '$DB_IP',/g" \
| sed -e "s/'PORT': 5432,/'PORT': $DB_PORT,/g" \
| sed -e "s/'USER': '<DB_USER>',/'USER': '$DB_USER',/g" \
| sed -e "s/'PASSWORD': '<DB_PASSWORD>'/'PASSWORD': '$DB_PASSWORD'/g" \
| sed -e "s/PUBLIC_URI = \"<PUBLIC_URI>\"/PUBLIC_URI = \"$PUBLIC_URI\"/g" \
> /tmp/settings.py

mv /tmp/settings.py Teamlock/settings.py

cat Teamlock/settings.py

# Waiting for postgresql to be ready to migrate
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_IP" -p "$DB_PORT" -U "$DB_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping..."
  sleep 1
done
>&2 echo "Postgres is up!"


# Migrate
python3 manage.py migrate

# Start Apache service
#service apache2 start
apachectl -D FOREGROUND