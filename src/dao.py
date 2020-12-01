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

    def store_user(self, username, password):
        user = None
        return user
      
    def verify_user_credentials(self, username, password):
        return bool
    
    def store_query(self, user, content):
        query = None
        return query
    
    def get_query_from_user(self, user, limit=5):
        return list
    
    def store_favorite_apod(self, user, apod_json):
        favorite_apod = None
        return favorite_apod

    def get_favorites_apod(self, user):
        return list
    
    def remove_favorite_apod(self, apod):
        return bool

    def store_graph(self, asteroid_json):
        graph_asteroid = None
        return graph_asteroid

    def get_graph(self, date):
        graph_asteroid = None
        return graph_asteroid

    def get_graph_points(self, date):
        return list
