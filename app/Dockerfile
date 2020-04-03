FROM python:3.7-stretch

RUN adduser kymry

WORKDIR /usr/src

COPY application/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn pymysql

COPY app app
COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP wsgi.py

RUN chown -R kymry:kymry ./
USER kymry

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]