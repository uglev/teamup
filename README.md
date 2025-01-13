# teamup.com (Python)
Please note that you must first replace the test data in the .env file:
- ACCESS_TOKEN: a token that can be obtained by requesting on the website https://teamup.com/api-keys/request (free),
- TEAMUP_PASSWORD: the password to your account on teamup.com,
- TELEGRAM_TOKEN: the token that you received when creating the telegram bot,
- CHAT_ID: the chat ID of your account, do not forget to write to the bot first before launching, otherwise it will not be able to write,
- SUBCALENDAR: the calendar number on the website teamup.com (secret calendar key), you must log in to your account and select Settings -> Sharing of your calendar -> "Create link".

It can be run once a day via crontab.

For everything else, see the documentation:
- https://www.postman.com/teamup-calendar/teamup-calendar-public-workspace/documentation/9dxuvwb/teamup-calendar-api-examples
- https://apidocs.teamup.com/

# Программа, которая считывает расписание с сайта teamup.com и отсылает в телеграмм список встреч на завтра (написана на питоне)
Обратите внимание, что сначала необходимо заменить тестовые данные в файле .env:
- ACCESS_TOKEN: токен, который можно получить путём запроса на сайте https://teamup.com/api-keys/request (бесплатно),
- TEAMUP_PASSWORD: пароль к Вашему аккаунту на teamup.com,
- TELEGRAM_TOKEN: токен, который Вы получили при создании телеграмм-бота,
- CHAT_ID: id чата Вашего аккаунта, не забудьте перед запуском написать боту первыми, иначе он писать не сможет,
- SUBCALENDAR: чтобы были видны только Ваши встречи, а не всей команды, необходимо получить номер своих встреч,
- ID: номер календаря на сайте teamup.com (secret calendar key), необходимо произвести логин в аккаунте и выбрать Settings -> Sharing of your calendar -> "Create link".

Запуск можно производить один раз в день посредством crontab. Например:
0 18 * * *  /usr/local/bin/python3 /usr/home/test/main.py

Во всём остальном смотрите документацию:
- https://www.postman.com/teamup-calendar/teamup-calendar-public-workspace/documentation/9dxuvwb/teamup-calendar-api-examples
- https://apidocs.teamup.com/
