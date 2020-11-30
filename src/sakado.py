import json
import os
import sys

import peewee

import dao
import model



class Sakado:
    def __init__(self, database_name):
        self.logged_user = None
        self.api_key = None
        self.dao = dao.DAO(peewee.SqliteDatabase(database_name))

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
    database_name = "nasa.db"
    application = Sakado(database_name)