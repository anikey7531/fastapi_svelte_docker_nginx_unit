# FROM nginx/unit:1.29.1-python3.11
FROM unit:1.31.1-python3.11

LABEL authors="anikey"

# устанавливаем зависимости нашего проекта
WORKDIR /code
COPY ./backend/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY config.json /docker-entrypoint.d/config.json
#копирую приложение
COPY  --chown=unit:unit ./backend/app /code/app
# копирую статику
COPY  --chown=unit:unit ./frontend/myspa/build /code/static
