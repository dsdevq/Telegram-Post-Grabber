# Grabber

## _Гайд по настройке и использованию_

Прежде чем запустить программу нам нужно настроить конфиг-файл.

Вот как сейчас выглядит config.json:
```json
{
  "client": {
    "api_id": 0,
    "api_hash": ""
  },
  "bot": {
    "token": "",
    "all_ID": [],
    "message": "Скрипт запущен!"
  },
  "settings": {
    "my_channels": [],
    "chats": [],
    "timer": 0,
    "ban_words": []
  }
}
```

### client
Чтобы получить данные ниже нам нужно перейти сюда: 
[https://my.telegram.org/](https://my.telegram.org/), 
тут залогинится, далее нажимаем "API development tools" и заполняем поля как-то [так](https://imgur.com/a/NCCkWrY) 
и не забываем поставить галочку в категории Platform на Desktop.
 - **api_id**: Первое поле, "App api_id", цифры, в категории "App configuration". 
В конфиг указывать как цифры. _Пример:_ 123456789
 - **api_hash**: Второе поле, "App api_hash", большой текст, в категории "App configuration". 
В конфиг указывать как строку, в кавычках. _Пример:_ "1a2b3c4_5#67s8fg9tty"

[Примеры этих полей](https://imgur.com/a/NjzxOYw)
### bot
 - **token**: Токен Вашего бота в Telegram, который нужен для работы самого бота. 
Бот будет предназначен для отправки пользователям сообщений о запуске софта и его ошибках во время работы. 
Получить можно [тут](https://t.me/BotFather). затем создайте нового бота, отправив/newbotкоманду. Следуйте инструкциям, 
пока не получите имя пользователя и токен для своего бота. 
Вы можете перейти к своему боту, перейдя по этому URL: ```https://telegram.me/YOUR_BOT_USERNAME``` 
и ваш токен должен выглядеть следующим образом: ```704418931:AAEtcZ*************```
В конфиг указывать как строку, в кавычках. _Пример:_ "703468982:AAEtcZ67s8fg9t3s4va4tty"
 - **all_ID**: Айди пользователей, которые будут получать от бота уведомления 
(чтобы их получать им нужно будет хоть раз зайти в бота и нажать /start)
Получить их можно [тут](https://t.me/myidbot) переслав в бота сообщение человека и скопировав нужный ID.
В конфиг указывать как массив цифр. _Пример:_ [123456789, 234567890, 345678901]
 - **message**: Уведомление, которое будет приходить при запуске софта.
В конфиг указывать как строку, в кавычках. _Пример:_ "Starting grabber..."
### settings
 - **my_channels**: Айди твоих каналов, в которые Вы хотите отправлять посты.
Получить их можно [тут](https://t.me/myidbot) переслав в бота сообщение с канала и скопировав нужный ID.
В конфиг указывать как массив цифр. _Пример:_ [123456789, -100234567890, -100345678901]
 - **chats**: Айди чужых каналов, из которых Вы хотите получать посты.
Получить их можно [тут](https://t.me/myidbot) переслав в бота сообщение с канала и скопировав нужный ID.
В конфиг указывать как массив цифр. _Пример:_ [-100123456789, 234567890, -100345678901]
 - **timer**: Таймер, через сколько секунд нужно отправлять пост в канал после публикации чужого канала.
В конфиг указывать как цифры. Ноль - без задержки. _Пример:_ 60
 - **ban_words**: Слова, по которым будут игнорироваться посты. 
Если в посте будет найдено слово из списка, то пост не будет опубликован у Вас.
В конфиг указывать как массив строк, в кавычках. _Пример:_ ["слово1", "слово2", "слово3]

Пример заполненого config.json:
```json
{
  "client": {
    "api_id": 123456789,
    "api_hash": "1a2b3c4_5#67s8fg9tty"
  },
  "bot": {
    "token": "703468982:AAEtcZ67s8fg9t3s4va4tty",
    "all_ID": [123456789, 234567890, 345678901],
    "message": "Starting grabber..."
  },
  "settings": {
    "my_channels": [123456789, 234567890, 345678901],
    "chats": [123456789, 234567890, 345678901],
    "timer": 0,
    "ban_words": ["слово1", "слово2", "слово3"]
  }
}
```

### Первый запуск софта

Все действия ниже нужно сдеать 1 раз или после того, когда будете что-то делать с файлами. 

Когда вы запустите софт Вас попросит ввести номер "Please enter your phone (or bot token): ", 
который Вы использовали выше и код подтверждения "Please enter the code you received: ".
Если у Вас стоит 2fa, то введите от неё пароль "Please enter your password: " (он отображаться в консоли не будет, но ввод работает).

После этого Вам напишет "Signed in successfully as ..." и софт будет работать.

### Запуск софта

Запускаете софт и он работает!