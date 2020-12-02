import datetime
import peewee
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
        try:
            user = model.user.User.create(username=username, password=password)
            return user
        except peewee.IntegrityError:
            return None
    
    def verify_user_credentials(self, username, password):
        try:
            user = model.user.User.get(username=username)
        except:
            return False
        
        try:
            user = model.user.User.get(username=username, password=password)
            return user
        except:
            return True
    
    def store_query(self, user_id, content):
        return model.query.Query.create(user_id=user_id, date=datetime.datetime.now(), content=content)
    
    def get_query_from_user(self, user, limit=5):
        return model.query.Query.select().limit(limit)
    
    #TODO
    def store_favorite_apod(self, user, apod_json):
        pass

    def get_favorites_apod(self, user):
        return model.favoriteapod.FavoriteAPOD.get(user_id=user.id)
    
    def remove_favorite_apod(self, apod):
        deleted_row = apod.delete_instance()
        if deleted_row == 1:
            return True
        else:
            return False

    #TODO
    def store_graph(self, asteroid_json):
        pass

    def get_graph(self, date):
        return model.graphasteroid.GraphAsteroid.get(date=date)

    def get_graph_points(self, date):
        graph_id = self.get_graph(date).id
        return model.graphasteroid.GraphAsteroid().get(graph_asteroid_id=graph_id)
