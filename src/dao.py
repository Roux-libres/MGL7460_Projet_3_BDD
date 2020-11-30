from playhouse.sqlite_ext import SqliteExtDatabase

import model



class DAO:
    def __init__(self, database_name):
        self.database = SqliteExtDatabase(database_name, 
                                              pragmas = {
                                                  'cache_size': -1 * 64000,
                                                  'foreign_keys': 1})
        
        self.database.connection()
        
        tables_list = [
                       model.favoriteapod.FavoriteAPOD,
                       model.graphasteroid.GraphAsteroid,
                       model.point.Point,
                       model.query.Query,
                       model.user.User
        ]
        self.database.create_tables(tables_list)

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
        return model.graphasteroid

    def get_graph_points(self, date):
        return list
