# Dockerize a flask app
FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5100
CMD ["python3", "server.py"]