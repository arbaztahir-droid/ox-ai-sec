FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir urllib3
CMD ["python", "-c", "print('container started')"]