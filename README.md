Из библиотек требуется только aiogram и environs.
Это что касаемо библиотек, так же требуется поместить файл '.env' в директорию 'election_bot_project', файл должен находиться на одном аерархическом уровне с файлом 'bot.py'.
В файле 'env' должен быть указан токен бота через пары ключ=значение, например:"token=какой-то токен'(ключом должно быть именно слово 'token', в противном случае функция в файле конфига не найдет ваш токен по иному ключу, и бот не запустится)