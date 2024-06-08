My Tasks
=======
Telegram bot that maintaining tasks. It can create, delete, update tasks. 

## How to run bot

* get your telegram api hash, id and get bot token from BotFather
* copy project files to your device
* rename the `.env.example` file to `.env`
* change the content of the `.env` file according to your parameters (for example BOT_TOKEN from BotFather)
* run docker compose `docker compose up`
* go to your bot and enjoy

## Technologies

| Technology | Why do I use?                                                                            |
|------------|------------------------------------------------------------------------------------------|
| Pyrogram   | It is asynchronous powerful MTPROTO Lib                                                  |
| Sqlalchemy | One of the most popular python's ORM                                                     |
| Alembic    | Good works with Sqlalchemy                                                               |
| Postgresql | Free, reliable database                                                                  |
| Redis      | Used for FSM. Redis is more powerful, more popular, and better supported than memcached. |
| Sqladmin   | WEB admin panel for this bot                                                             |





