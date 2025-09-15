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


Правильно — по умолчанию у пользователя postgres нет пароля, и подключение к базе происходит через аутентификацию peer (т.е. если ты зашёл в систему под тем же Linux-пользователем postgres).
Примеры:

Это работает:

    sudo -u postgres psql

А вот это — не сработает, пока не задан пароль и не включена md5-аутентификация:

    psql -U postgres -W

🔐 Как задать пароль пользователю postgres

Войти под postgres:

    sudo -u postgres psql

Выполнить SQL:

    \password postgres

Ввести новый пароль дважды. После этого выйди из psql:

    \q

🛠️ Затем — разреши вход по паролю

Открой:

    sudo nano /etc/postgresql/*/main/pg_hba.conf

И замени peer на md5 для строк local и host, например:

    local   all             postgres                                md5
    host    all             all             127.0.0.1/32            md5

Перезапусти:

    sudo systemctl restart postgresql

Теперь ты можешь подключаться по паролю:

    psql -U postgres -h 127.0.0.1 -W
