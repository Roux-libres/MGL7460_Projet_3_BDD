import datetime
import peewee

import model



class DAO:
    def __init__(self, database_name):
        self.database = peewee.SqliteDatabase(database_name)
        
        self.database.connect()
        
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
        try:
            graphasteroid = model.graphasteroid.GraphAsteroid.create(date=date.strftime('%Y-%m-%d'))
        except:
            pass
        
        try:
            for asteroid in asteroid_json['near_earth_objects'][date.strftime('%Y-%m-%d')]:
                model.point.Point.create(graph_asteroid_id=graphasteroid.id,
                                         distance=float(asteroid['close_approach_data'][0]['miss_distance']['kilometers']),
                                         radius=(float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']) + float(asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'])) / 2)
        except Exception as e:
            print("Exception :", e)
            has_encountered_error = True
        return not has_encountered_error

    def get_graph(self, date):
        try:
            return (model.graphasteroid.GraphAsteroid.select(model.graphasteroid.GraphAsteroid.id).where(model.graphasteroid.GraphAsteroid.date == date.strftime('%Y-%m-%d')))[0]
        except:
            return None

    def get_graph_points(self, date):
        try:
            graph_id = self.get_graph(date)
            return (model.point.Point.select(model.point.Point.distance, model.point.Point.radius).where(model.point.Point.graph_asteroid_id == graph_id))
        except:
            return []
