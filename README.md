# Реализация функционала гостя

# Установка

1. Клонируйте репозиторий:

```bash
   git clone https://github.com/aekkakti/studio.git

```

2. Перейдите в директорию проекта:

```bash
    cd studio
```

3. Установите зависимости:

```bash
    pip install django
    pip install django-bootstrap4
    pip install Pillow
```

# Запуск

1. Выполните миграции базы данных:

```bash
    python manage.py makemigrations
    python manage.py migrate
```

2. Запустите сервер:

```bash
    python manage.py runserver
```

3. Вход в панель администратора осуществлять по адресу:

```bash
    http://localhost:8080/superadmin/
```

```bash
    Логин: admin
    Пароль: admin
```

## Автор

Выполнил Иванов Гордей, 421 группа
