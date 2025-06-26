### 🔧 Установка Redis на Ubuntu (подходит для Ubuntu 20.04, 22.04, 24.04)
## 1. Обнови систему

    sudo apt update && sudo apt upgrade -y

## 2. Установи Redis

    sudo apt install redis -y

## 3. Проверь, работает ли Redis

    sudo systemctl status redis

        Должно быть написано active (running)

## 4. (Опционально) Разреши автозапуск Redis

    sudo systemctl enable redis

## 5. Проверь подключение к Redis

    redis-cli ping

    Ответ должен быть PONG

# и🛡 Настройка (по желанию)

# иФайл конфигурации Redis:
/etc/redis/redis.conf

# иПример: разрешить подключение по сети (по умолчанию Redis слушает только 127.0.0.1):

    sudo nano /etc/redis/redis.conf

# иНайди строку:

    bind 127.0.0.1 ::1

# и замени на:

    bind 0.0.0.0

# Также измени:

    protected-mode yes

# на:

    protected-mode no

# Перезапусти Redis после изменения:

    sudo systemctl restart redis
