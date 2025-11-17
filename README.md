# API для управления библиотекой
REST API для управления библиотекой. API предоставляет возможности для управления книгами, авторами и 
пользователями, а также отслеживает выдачи книг пользователям. 
Для реализации API использовать Django Rest Framework (DRF).

# Инструкция по установке и использованию разработанного функционала приложения
1. Клонируйте репозиторий:
```
git clone https://github.com/4usnok/library_manage_api.git
```
2. Установите зависимости:
```
poetry install
```
3. Активировать окружение
```
poetry env activate
```

# Содержание проекта

## Приложение `authors`  
1. `models.py`:  
Authors -> Модель для авторов  
2. `view.py`:  
AuthorsList -> Просмотр списка авторов,  
AuthorsCreate -> Создание автора,  
AuthorsDestroy -> Удаление автора,  
AuthorsUpdate -> Редактирование автора,  
AuthorsRetrieve -> Просмотр подробной информации об авторе  
3. `serializers.py`:  
AuthorsSerializer -> Сериализатор для модели `Authors`  

## Приложение `books`  
1. `models.py`:  
Books -> Модель для книг  
2. `view.py`:  
BooksList -> Просмотр списка книг  
BooksCreate -> Создание книги  
BooksDestroy -> Удаление книги  
BooksUpdate -> Редактирование книги  
BooksRetrieve -> Просмотр одной книги  
3. `serializers.py`:  
BooksSerializer -> Сериализатор для модели `Books`  

## Приложение `genre`  
1. `models.py`:  
Genre -> Модель для жанра  
2. `view.py`:  

3. `serializers.py`:  
GenreSerializer -> Сериализатор для модели `Genre`  

# Работа с программой  
1. Запуск сервера осуществляется командой: `python manage.py runserver`  
2. Ручное создание и запуск контейнера:  
`docker run -d `  
--name my-django-employee-task `  
-p 8000:8000 `  
-v employee-task-media-volume:/empoyee-task/media `  
-e DEBAG=1 `  
my-django-employee-task `  
3. Запуск бота производится из корневой директории: `python bot.py`  

# Полезные команды  
* Запуск виртуального окружения poetry: `poetry env activate`  
* Запуск сервера: `python manage.py runserver`,  
* Создание суперюзера(админка): `python manage.py createsuperuser`,  
* Создание миграций: `python manage.py makemigrations`,  
* Сохранение миграций: `python manage.py migrate`,  
* Откат всех миграций: `python manage.py migrate name_migration`, где `name_migration` -> название миграции.  
* Создания файла с покрытием `.coverage`: `coverage html`  
* Посмотреть покрытие unit-тестами: `coverage report`  
* Запуск обработчика очереди (worker) для получения задач и их выполнения: `celery -A config worker -l INFO`  
* Запуск redis-server: `./redis-server.exe`  
* Запуск redis-cli: `./redis-cli.exe`  
* Сборка образа: `docker build -t my-django-employee-task .`  
* Запуск контейнера: `docker run -p 8000:8000 my-django-employee-task`  
* Просмотр контейнеров: `docker images`  
* Вывод логов контейнеризации: `docker-compose logs db`  
* Запускает все сервисы, определенные в файле: `docker-compose up`  
