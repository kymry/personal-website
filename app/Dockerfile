FROM python:3.8-slim-buster

RUN adduser kymry

WORKDIR /usr/src

COPY application/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn pymysql

COPY application application
COPY migrations migrations
COPY wsgi.py wsgi.py
COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP wsgi.py

RUN chown -R kymry:kymry ./
USER kymry

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]