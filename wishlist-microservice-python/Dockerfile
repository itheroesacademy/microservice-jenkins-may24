
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1003

ENV FLASK_APP=index.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=1003"]
