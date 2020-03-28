FROM python:3.8

# We want stdout and stderr to be buffered
ENV PYTHONBUFFERED 1

# Installing the requirements
RUN apt-get update \
&& apt-get install -y \
        apache2 \
        libapache2-mod-wsgi-py3 \
        libpq-dev \
        postgresql-client \
&& rm -rf /var/lib/apt/lists/*

# Let's install the python env
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# We put the sources in the /app directory
RUN mkdir /app /var/log/teamlock
COPY api /app/api
COPY doc /app/doc
COPY gui /app/gui
COPY Teamlock /app/Teamlock
COPY teamlock_toolkit /app/teamlock_toolkit
COPY manage.py /app/manage.py
COPY docker/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Enabling apache mods and sites
RUN a2enmod \
        ssl \
        wsgi \
        rewrite \
        expires \
        proxy_http \
 && a2dissite 000-default

WORKDIR /app

EXPOSE 80/tcp

ENTRYPOINT [ "/entrypoint.sh" ]