import json
import os
import sys

import peewee

import dao
import model



class Sakado:
    def __init__(self, database_name, database_path=""):
        self.logged_user = None
        self.api_key = "DEMO_KEY"
        self.api_queries = {
            "apod"      : "https://api.nasa.gov/planetary/apod?",
            "asteroid"  : "https://api.nasa.gov/neo/rest/v1/feed?",
            "earth"     : "https://api.nasa.gov/planetary/earth/imagery?"
        }
        self.dao = dao.DAO(os.path.join(database_path, database_name))

    def display_login_screen(self):
        pass

    def sign_up(self, username, password):
        pass

    def log_in(self, username, password):
        pass

    def display_choices(self):
        pass

    def manage_query(self):
        pass

    def fetch_data(self, url, parameters):
        return json

    def get_user_input(self, message):
        return ""

    def display_menu(self, messages):
        pass
    
    def display_APOD_features(self):
        pass

    def display_favorites_APOD(self):
        pass

    def display_earth_feature(self):
        pass

    def display_asteroid_features(self):
        pass

    def display_queries(self):
        pass

if __name__ == "__main__":
    database_name = "database.db"
    application = Sakado(database_name, database_path=os.path.abspath(os.path.dirname(__file__)))
    