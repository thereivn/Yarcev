FROM python:3.9

# Установка Flask
RUN pip install --no-cache-dir flask

# Копирование исходного кода
COPY ./src /app

# Установка рабочего каталога
WORKDIR /app

# Открытие порта
EXPOSE 80

# Запуск приложения
CMD ["python", "main.py"]