FROM python:2
COPY . /src/remote-tail
CMD python /src/remote-tail/server.py
EXPOSE 8080