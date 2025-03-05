# FOR LAB №1 in ./1lab/py-flask
## Установка и запуск через Docker
### 1. Сборка образа
```bash
docker build -f ./1lab/py-flask/pyf.dockerfile -t lab1-pyfl ./1lab/py-flask
```
### 2. Запуск
```bash
docker run --rm -d --name pyapp -p 80:80 lab1-pyfl
```
### 3. Ссылка
```bash
http://localhost/
```
# FOR LAB №2 in ./2lab/main.py
## Установка и запуск через Docker
### 1. Сборка образа
```bash
docker build -f ./2lab/2lab.dockerfile -t lab2-py ./2lab
```
### 2. Запуск
```bash
docker run --rm --name pyapp2 lab2-py 
```

## Остановить контейнеры и удалить образы
```bash
docker stop pyapp pyapp2
```
```bash
docker rmi lab1-pyfl lab2-py 
```