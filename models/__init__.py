#!/usr/bin/python3
import pymysql
from models.db_storage_engine.storage import DBStorage

pymysql.install_as_MySQLdb()
storage = DBStorage()
storage.reload()
