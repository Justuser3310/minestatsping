## Что это?

Это проект, который предоставялет: простого онлайн ТГ бота ; аналитику сервера по типу пинг сервера, количество игроков.

<img src="https://gitea.404.mn/justuser/minestatsping/raw/branch/main/preview/2024-03-09_12-20.png" alt="drawing" width="400"/>

## Как использовать?

### Использование ТГ бота

1. Получить токен в https://t.me/BotFather
2. Запустить: `python online.py`
3. Вставить токен в `config.json`, где написано "token"
4. Запустить: `python online.py`
5. Проверить команду бота: `/online`

### Использование аналитики

1. Указать данные сервера в `ping.py`
    - адрес - host
    - порт - port
    - протокол - prot ( https://minecraft.fandom.com/wiki/Protocol_version#Java_Edition )
2. Запустить сбор статистики: `python ping.py`
3. Запустить сайт: `python site_stat.py`
4. Зайти на сайт: `127.0.0.1:8050` (браузер)