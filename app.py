import logging.config
import datetime
import os

from flask import Flask
from flask_cors import CORS
import settings
from bot.chat import bot_reply, bot_name

app = Flask(__name__)
log = logging.getLogger(__name__)
CORS(app)


@app.route('/')
def home():
    return 'Home Page. Nothing here :('


@app.route('/bot/<stmt>')
def chat_bot(stmt):
    print(stmt)
    resp_stmt = bot_reply(stmt)
    cur_time = datetime.datetime.now()
    timestamp = cur_time.strftime("%b %d, %H:%M")
    return {"bot": {"name": bot_name, "chat": resp_stmt, "timestamp": timestamp}}


def configure_app(flask_app):
    pass


def initialize_app(flask_app):
    configure_app(flask_app)
    print("App Initialization Complete!")


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host=settings.FLASK_SERVER_HOST, port=settings.FLASK_SERVER_PORT, debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()