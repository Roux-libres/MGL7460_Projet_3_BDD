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
        try:
            return model.query.Query.select().limit(limit)
        except:
            return []
    
    #TODO
    def store_favorite_apod(self, user, apod_json):
        pass

    def get_favorites_apod(self, user):
        try:
            return model.favoriteapod.FavoriteAPOD.get(user_id=user.id)
        except:
            return None
    
    def remove_favorite_apod(self, apod):
        deleted_row = apod.delete_instance()
        if deleted_row == 1:
            return True
        else:
            return False

    def store_graph(self, date, asteroid_json):
        has_encountered_error = False
        graphasteroid = model.graphasteroid.GraphAsteroid.create(date=date)
        try:
            for asteroid in asteroid_json['near_asteroid_objects'][date.strptime('%Y-%m-%d')]:
                model.point.create(graph_asteroid_id=graphasteroid.id,
                                   distance=asteroid['close_approach_data']['miss_distance']['kilometers'],
                                   radius=(asteroid['estimated_diameter']['kilometers']['estimated_diameter_min'] + asteroid['estimated_diameter']['kilometers']['estimated_diameter_max']) / 2)
        except:
            has_encountered_error = True
        return not has_encountered_error

    def get_graph(self, date):
        try:
            return model.graphasteroid.GraphAsteroid.get(date=date)
        except:
            return None

    def get_graph_points(self, date):
        graph_id = self.get_graph(date).id
        return model.graphasteroid.GraphAsteroid().get(graph_asteroid_id=graph_id)
