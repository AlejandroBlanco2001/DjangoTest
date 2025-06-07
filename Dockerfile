FROM python:3.12-slim

RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . /app/

EXPOSE 8000

RUN chmod +x prepare_server.sh
CMD ["./prepare_server.sh"]