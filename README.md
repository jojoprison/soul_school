# Soul School

Проект менеджмента уроков обучающей платформы.


### Предустановки

- `docker` на локальном компьютере (+ `wsl` в случае `Windows`)


## Билд проекта
- предварительно скопировать и настроить (опционально) `.env.tmp` -> `.env` в корне проекта
- `docker-compose up --build -d` - билдим и запускаем проект, не блокируя консоль
- `docker compose exec back_end python manage.py createsuperuser` - создаем админа
- `poetry install --only dev` - для установки dev-зависимостей при необходимости отладки проекта

## Работа проекта

- переходим на `http://127.0.0.1/`
- вводим креды админа, созданного ранее
- должен открыться список уроков
- - при рефреше страницы также отобразится список уроков
- - при переходе по другим любым url помимо `/login` и `/lessons` произойдет редирект на `/login`

## Проверка API через Postman
- предварительно сгенерировать `access_token` `http://127.0.0.1/api/v1/auth/jwt/create/`, передав username + пароль
- прокинуть токен в headers: `Authorization : JWT <access_token>`
- информация о юзере: `http://127.0.0.1/api/v1/auth/users/me/`
- список доступных уроков: `http://127.0.0.1/api/v1/lessons/`
- список доступных уроков по конкретному продукту: `http://127.0.0.1/api/v1/products/2/lessons/`
- статистика по всем продуктам: `http://127.0.0.1/api/v1/products-statistics/`
