# Описание
Стартовый проект который включает в себя все необходимые базовые компоненты для начала разработки проекта 

# Общая схема
![img_1](files/img/scheme1.jpg)
Дополнительная информация доступна в readme каждого компонента

|   |  |
| ------------- | ------------- |
| Frontend  | [Readme.md](./services/frontend/README.md)  |
| Backend  | [Readme.md](./services/backend/README.md)  |


# Доступность ресурсов  
`frontend/nuxtjs` - `http://localhost:1338/`

`backend/django` - `http://localhost:1338/admin/`

`backend/sphinx` - `http://localhost:1338/docs/`

`db/adminer` - `http://localhost:8099/`

# Структура каталогов
```
find . ! -path "./.git/*" ! -path "./services/frontend/node_modules/*" ! -path "./services/postgres/db/*" ! -path "./services/frontend/.nuxt/*" ! -path "./services/backend/docs/*" ! -path "./services/backend/.ruff_cache/*"
```

```
.
./services
./services/frontend
./services/frontend/Dockerfile
./services/frontend/node_modules
./services/frontend/tsconfig.json
./services/frontend/.env.example
./services/frontend/nuxt.config.ts
./services/frontend/README.md
./services/frontend/package-lock.json
./services/frontend/.nuxt
./services/frontend/tailwind.config.ts
./services/frontend/app
./services/frontend/app/assets
./services/frontend/app/assets/css
./services/frontend/app/assets/css/main.css
./services/frontend/app/layouts
./services/frontend/app/layouts/default.vue
./services/frontend/app/layouts/empty.vue
./services/frontend/app/pages
./services/frontend/app/pages/index.vue
./services/frontend/app/app.vue
./services/frontend/.env
./services/frontend/package.json
./services/frontend/public
./services/frontend/public/avatar
./services/frontend/public/avatar/1.png
./services/frontend/public/favicon.ico
./services/frontend/public/robots.txt
./services/frontend/.gitignore
./services/nginx
./services/nginx/Dockerfile
./services/nginx/nginx.conf
./services/backend
./services/backend/Dockerfile
./services/backend/pyproject.toml
./services/backend/Pipfile
./services/backend/gunicorn.py
./services/backend/.ruff_cache
./services/backend/.env.example
./services/backend/run_before.sh
./services/backend/docs
./services/backend/README.md
./services/backend/Pipfile.lock
./services/backend/settings
./services/backend/settings/urls.py
./services/backend/settings/settings.py
./services/backend/settings/wsgi.py
./services/backend/settings/__init__.py
./services/backend/settings/asgi.py
./services/backend/apps
./services/backend/apps/testapp
./services/backend/apps/testapp/views.py
./services/backend/apps/testapp/tests.py
./services/backend/apps/testapp/models.py
./services/backend/apps/testapp/migrations
./services/backend/apps/testapp/migrations/0002_alter_project_title_comments.py
./services/backend/apps/testapp/migrations/__init__.py
./services/backend/apps/testapp/migrations/0001_initial.py
./services/backend/apps/testapp/apps.py
./services/backend/apps/testapp/__init__.py
./services/backend/apps/testapp/factories.py
./services/backend/apps/testapp/admin.py
./services/backend/apps/sphinx_docs
./services/backend/apps/sphinx_docs/views.py
./services/backend/apps/sphinx_docs/tests.py
./services/backend/apps/sphinx_docs/models.py
./services/backend/apps/sphinx_docs/urls.py
./services/backend/apps/sphinx_docs/migrations
./services/backend/apps/sphinx_docs/migrations/__init__.py
./services/backend/apps/sphinx_docs/apps.py
./services/backend/apps/sphinx_docs/__init__.py
./services/backend/apps/sphinx_docs/admin.py
./services/backend/apps/__init__.py
./services/backend/.env
./services/backend/run_before.py
./services/backend/.gitignore
./services/backend/manage.py
./services/backend/static
./services/postgres
./services/postgres/db
./services/postgres/.gitignore
./README.md
./docker-compose.yaml
./.git
./dir.txt
./FORMYSELF.md
./files
./files/git
./files/git/pre-commit
./files/img
./files/img/scheme1.jpg
./.gitignore

```

# Установленные и настроенные модули для backend и frontend

## Backend/Django
```
[packages]
django = "*"
djangorestframework = "*"
gunicorn = "*"
python-dotenv = "*"
psycopg2-binary = "*"
sphinx = "*"
sphinx-rtd-theme = "*"
sphinxcontrib-django = "*"

[dev-packages]
django-debug-toolbar = "*"
ruff = "*"
django-extensions = "*"
factory-boy = "*"
faker = "*"
```
`cd services/backend && pipenv graph` для получения дополнительной информации

## Frontend/Nuxtjs
```
├── @emnapi/core@1.7.1 extraneous
├── @emnapi/runtime@1.7.1 extraneous
├── @emnapi/wasi-threads@1.1.0 extraneous
├── @iconify-json/lucide@1.2.75
├── @napi-rs/wasm-runtime@1.0.7 extraneous
├── @nuxt/icon@2.1.0
├── @nuxt/ui@4.2.1
├── @nuxtjs/tailwindcss@6.14.0
├── @tybys/wasm-util@0.10.1 extraneous
├── nuxt@4.2.1
├── typescript@5.9.3
├── vue-router@4.6.3
└── vue@3.5.25
```
`cd services/frontend && npm list` для получения дополнительной 


# Установка и настройка
```
git clone <repo_name> <project_name>
```
Выполните настройки backend 
```
cp services/backend/.env.example services/backend/.env
```
Укажите необходимые нараметры подключения к базе данных а также django `SECRET_KEY`
```
cd services/backend/
pipenv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
По умолчанию `nginx` стартует на порту `1338`. Если данный порт у вас занят то необходимо внести изменения в `docker-compose.yaml`. Внесите изменения в секцию `ports` 

```
service.nginx:
    build:
      context: .
      dockerfile: ./services/nginx/Dockerfile
    ports:
      - 1338:80 # Измените 1338 на любой другой свободный локальный порт. Например, 1340
    depends_on:
      - service.frontend
    volumes:
      - static_volume:/usr/share/nginx/html/static
    restart: unless-stopped
    networks:
      - internal-net
```
Первый запуск - собрать и запустить
```
docker compose up --build
```
Последующие запуски с учетов отсутствия изменения в конфигурации можно производить без `--build`
```
docker compose up
```



# Для локальной работы вам понадобятся:

1. Docker Decktop (Управление контейнерами)
2. python3 (Backend/django)
3. pipenv (Backend/django)
4. nodejs (Fontend/nuxtjs)
5. npm (Fontend/nuxtjs)


# Известные проблемы
## `pre-commit`и собственный велосипед
Модуль `pre-commit` работает относительно текущей папки запуска git. В данном шаблоне приложения структура папок организованна по другому. В целом все работает также просто на самописном `sh` скрипте без использования модуля `pre-commit`. Также немного изменена логика - git commit не пройдет если есть любые изменения `ruff format`. Поэтому счала `ruff fromat` а потому уже `git commit` 

Подробнее тут `files/git/pre-commit`

# Roadmap
## Перейти с `pipenv` на `uv`
В `pipenv` есть возможность хранить окружение за пределами рабочей паки проекта. Это позволяет чистить диск простым удалением всех окружений из одной папки. Для восстановления окружения достаточно выполнить `pipenv sync --dev`.

 Это пока единственная причина почему еще не `uv`

## Перейти с django/drf на FastAPI
Это тестовый проект. Хочется пощупать всё. В перспективе просто добавится +1 микросервис а уж подключать его или нет это дело каждого.