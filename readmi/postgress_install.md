Чтобы установить PostgreSQL на Ubuntu, выполни следующие шаги:
✅ Шаг 1: Обнови список пакетов

    sudo apt update

✅ Шаг 2: Установи PostgreSQL

sudo apt install postgresql postgresql-contrib

    postgresql — основной сервер базы данных

    postgresql-contrib — полезные расширения (например, uuid-ossp, pg_stat_statements)

✅ Шаг 3: Проверь статус сервиса

    sudo systemctl status postgresql

Если всё работает, увидишь статус active (exited) или active (running).
✅ Шаг 4: Войти в PostgreSQL под пользователем postgres

    sudo -u postgres psql

Ты попадёшь в командную оболочку PostgreSQL (psql), где можешь выполнять SQL-запросы.

Пример:

    \l         -- список баз данных
    \q         -- выйти из psql

✅ Дополнительно: создать базу и пользователя

    sudo -u postgres createuser --interactive
    sudo -u postgres createdb mydb

Или в psql:

    CREATE USER myuser WITH PASSWORD 'mypassword';
    CREATE DATABASE mydb OWNER myuser;
    GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

✅ Разрешить подключения по паролю (опционально)

Открой файл pg_hba.conf:

    sudo nano /etc/postgresql/*/main/pg_hba.conf

Найди строки с local и host, замени peer на md5:

    local   all             postgres                                md5
    host    all             all             127.0.0.1/32            md5

Перезапусти PostgreSQL:

    sudo systemctl restart postgresql