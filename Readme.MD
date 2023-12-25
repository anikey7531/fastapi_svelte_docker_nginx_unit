FastApi + Svelte SPA + Docker + PostgreSQL + Unit (nginx)

Шаблон SPA приложения написанным на Svelte, в качестве REST сервера используется fastapi

В качестве web и app сервера выступает unit nginx. Все настроено в Docker контейнере и готово к развертыванию на сервере.

Установка запуск скрипта для формирования файла requirements.txt из poetry 
```
poetry_to_req.sh
```
в папке frontend/myspa установка статики
```
npm install
npm run build
```
запуск контейнера
```
docker-compose up 
```