# Перехватыватывает нажатия клавишь xbindkeys

### установка 
    sudo apt insta ll xbindkeys xdotool
### создатб конфиг
    xbindkeys --defaults > ~/.xbindkeysrc
### редактировать конфиг
    nano ~/.xbindkeysrc
##### применить конфиг
    xbindkeys -p
### Узнать какие клавиши нажимаются
    xev
### запуск
    xbindkeys       запуск
    xbindkeys -s    посмотреть бинды
