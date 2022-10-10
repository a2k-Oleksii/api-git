FROM python:3.8

COPY main.py /script/main.py

WORKDIR /script

RUN apt-get update && apt-get install -y iputils-ping

CMD ["python", "main.py"]