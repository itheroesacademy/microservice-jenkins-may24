
FROM python:3.9
WORKDIR /app
COPY . .
RUN /bin/sh -c pip install --no-cache-dir -r requirements.txt
RUN pip install pytest
EXPOSE 1003
CMD ["python", "index.py"]
