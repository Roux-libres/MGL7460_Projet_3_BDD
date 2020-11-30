from peewee import SqliteDatabase

import model
db = SqliteDatabase("nasa.db")

class DAO:
    def __init__(self):
        pass

    def get_query_from_user(self, user, limit=5):
        return list

    def store_query(self, user, content):
        return bool
    
    def get_favorite_APOD_from_user(self, name, url):
        return list

    def add_APOD_to_favorites(self, name, url):
        return bool
    
    def remove_APOD_to_favorites(self, apod):
        return bool

    def store_graph(self, asteroid_json):
        pass

    def get_graph(self, date):
        return model.GraphAsteroid

    def get_graph_points(self, date):
        return list


