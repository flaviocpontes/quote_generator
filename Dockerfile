FROM python:3.7.4-alpine

RUN pip install aiohttp==3.6.1

EXPOSE 8080

ADD . .

CMD python app.py