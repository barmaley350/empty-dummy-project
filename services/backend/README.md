# Установка и настройка
## Предустановленные модули
1. Django REST Framework (DRF)
2. Django DevTools 
3. Ruff
4. django_extensions

## Установка проекта
Устанавливаем проект `settings` в текущую директорю без создания дополнительной подпапки

```
pipenv run django-admin startproject settings .
```

Полный путь будет `<project_name>/backend/settings`

## Создание приложений
Приложения будут храниться в отдельной папке `apps` для более удобной организации структуры проекта. Перед создание приложения необходимо предварительно создать папку приложения. 

`mkdir apps/<app_name>` а затем выполнить

```
pipenv run python3 manage.py startapp <app_name> apps/<app_name>
```

После установки приложения необходимо изменить `name` в `apps/<app_name>/apps.py` на `apps.<app_name>`

Также не забываем добавить приложение в `settings/settings.py` в раздел `INSTALLED_APPS` в формате `apps.<apps_name>`

## Работа в Docker контейнере
### django_extensions / shell_plus
```
docker exec -it <project_name>-service.backend-1 pipenv run python3 manage.py shell_plus
```

`<project_name>` название папки корневого проекта. Также название контейнера можно посмотреть в Docker Desktop