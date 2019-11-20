FROM python:3.8.0

RUN pip install aiohttp==3.6.1

EXPOSE 8080

ADD . .

CMD python app.py