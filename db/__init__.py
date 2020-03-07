import sqlite3
import logging
import sys
from config import DB_NAME
import click
from flask import current_app
from flask.cli import with_appcontext


def get_db():
    _conn = None
    try:
        _conn = sqlite3.connect(DB_NAME)
    except sqlite3.Error:
        logging.error('数据库连接失败')
    return _conn


@click.command('init-db')
@with_appcontext
def init_db_command():
    logging.warning("正在初始化数据库")
    db = get_db()
    with current_app.open_resource(r'db\db_init.sql') as f:
        db.executescript(f.read().decode('utf8'))

