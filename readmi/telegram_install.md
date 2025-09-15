✅ Способ 1: Через Snap (рекомендуется)

    sudo snap install telegram-desktop

📦 Telegram обновляется автоматически.

🧱 Устанавливается как полноценное десктоп-приложение.
    
✅ Способ 2: Через .tar.xz архив с официального сайта

Перейди на: https://desktop.telegram.org

Скачай Linux-версию (обычно tsetup.X.Y.Z.tar.xz)

Распакуй архив:

    tar -xf tsetup.*.tar.xz
    cd Telegram

Запусти:

    ./Telegram

📌 Можно закрепить ярлык, чтобы запускать из меню. Спроси — помогу.

✅ Способ 3: Через APT из стороннего PPA (не рекомендуется)

Это устаревший способ, не всегда даёт последнюю версию:

    sudo add-apt-repository ppa:atareao/telegram
    sudo apt update
    sudo apt install telegram

✅ Проверка

После установки запусти:

    telegram-desktop

или найди в меню "Telegram".