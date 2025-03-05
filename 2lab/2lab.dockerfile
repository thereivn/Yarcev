FROM python:3.9
RUN pip install --no-cache-dir numpy
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]