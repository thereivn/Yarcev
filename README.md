## Установка и запуск через Docker
### 1. Сборка образа

```bash
docker build -f ./py-flask/pyf.dockerfile -t lab1-pyfl ./py-flask
```
### 2. Запуск

```bash
docker run --rm -d --name pyapp -p 80:80 lab1-pyfl
```
### 3. Ссылка

```bash
http://localhost/
```