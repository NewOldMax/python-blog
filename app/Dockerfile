FROM advancedclimatesystems/python:2.7.10
MAINTAINER Auke Willem Oosterhoff <auke@orangetux.nl>

COPY wheelhouse /wheelhouse

RUN pip install --no-index --find-links wheelhouse \
    flask \
    flask-redis \
    WTForms \
    Flask-WTF \
    six \
    uwsgi

COPY src /app
COPY uwsgi.ini /etc/uwsgi.ini
COPY shared_libs/* /lib/

CMD uwsgi --ini /etc/uwsgi.ini
