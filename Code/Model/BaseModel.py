#from peewee import SqliteDatabase

class BaseModel:
    def __init__(self):
        self.database = None