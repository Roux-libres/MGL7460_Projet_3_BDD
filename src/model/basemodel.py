import os

import peewee



DATABASE = peewee.SqliteDatabase(os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\..\src\database.db"))

class BaseModel(peewee.Model):
    class Meta:
        database = DATABASE