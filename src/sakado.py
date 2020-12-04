import datetime
import json
import math
import os
import requests
import sys
import webbrowser

import matplotlib.pyplot as plt

import dao
import model



class Sakado:
    def __init__(self, database_name, database_path=""):
        self.logged_user = None
        self.api_key = "arEyisNvZj8juScmQ16pfvvQ8V5fS7CX2ApJYDuS"
        self.api_queries = {
            "apod"      : "https://api.nasa.gov/planetary/apod?",
            "asteroid"  : "https://api.nasa.gov/neo/rest/v1/feed?",
            "earth"     : "https://api.nasa.gov/planetary/earth/imagery?"
        }
        self.dao = dao.DAO(os.path.join(database_path, database_name))

    def display_login_screen(self):
        menu = ["Welcome to the Sakado program",
                    "This program use the NASA's API (https://api.nasa.gov)",
                    "Would you like to log in (1) or sign up (2) ?"]
        self.display_menu(menu, True)
        
        number_of_try = 5
        can_continue = False
        
        while not can_continue and number_of_try > 0:
            choice = self.get_user_input("Please enter a number associated with an option : ")
            if choice == "1":
                username = self.get_user_input("Please enter your username : ")
                password = self.get_user_input("Please enter your password : ")
                self.log_in(username, password)
            elif choice == "2":
                username = self.get_user_input("Please enter a valid username : ")
                password = self.get_user_input("Please enter a valid password : ")
                self.sign_up(username, password)
            else:
                self.display_menu(["Invalid choice"])
            
            if isinstance(self.logged_user, model.user.User):
                can_continue = True
            else:
                number_of_try -= 1
                self.display_menu(["{} attempt(s) remaining".format(number_of_try)])
        
        if number_of_try == 0:
            self.display_menu(["Too many attempts",
                               "Application stopping"])
            return
        else:
            self.display_choices()

    def sign_up(self, username, password):
        result = self.dao.store_user(username, password)
        if isinstance(result, model.user.User):
            self.logged_user = result
            self.display_menu(["Account for user {} successfully created".format(self.logged_user.username)])
        else:
            self.display_menu(["Username already exists",
                               "Please enter another username"])

    def log_in(self, username, password):
        result = self.dao.verify_user_credentials(username, password)
        if isinstance(result, model.user.User):
            self.logged_user = result
            self.display_menu(["User {} successfully logged in".format(self.logged_user.username)])
        elif result:
            self.display_menu(["Wrong password"])
        else:
            self.display_menu(["There is not account associated with this username"])

    def display_choices(self):
        menu = ["Welcome {} to the Sakado program".format(self.logged_user.username),
                "This program use the NASA's API (https://api.nasa.gov)",
                "Please choose one of the following functionality :",
                "1) Display APOD functionalities",
                "2) Display Earth functionalities",
                "3) Display Asteroid functionalities",
                "4) Display your previous queries"]
        self.display_menu(menu, True)
        
        number_of_try = 5
        
        while number_of_try > 0:
            choice = self.get_user_input("Please enter a number associated with a functionality : ")
            if choice == "1":
                self.display_APOD_features()
                break
            elif choice == "2":
                self.display_earth_feature()
                break
            elif choice == "3":
                self.display_asteroid_features()
                break
            elif choice == "4":
                self.display_queries()
                break
            else:
                self.display_menu(["Invalid choice",
                                   "{} attempt(s) remaining".format(number_of_try)])
            
        if number_of_try == 0:
            self.display_menu(["Too many attempts",
                               "Disconnecting user {}".format(self.logged_user.username),
                               "Application stopping"])
            return

    #TODO
    def display_queries(self):
        pass

    def fetch_data(self, url, parameters):
        try:
            url += 'api_key=' + self.api_key
            for parameter in parameters:
                url += '&' + parameter + '=' + str(parameters[parameter])
            return requests.get(url).json()
        except:
            return None

    def get_user_input(self, message):
        return input(message)

    def clear_console(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
    
    def display_menu(self, messages, erase=False):
        if erase: self.clear_console()
        for message in messages:
            print(message)
    
    def open_url_in_browser(self, url):
        try:
            webbrowser.open(url)
        except:
            self.display_menu(["An error occurred during the opening of the URL"])
    
    #TODO
    def display_APOD_features(self):
        pass

    #TODO
    def display_APOD(self, apod_json):
        pass
        
    #TODO
    def display_favorites_APOD(self):
        pass
    
    #TODO
    def construct_web_page_APOD(self):
        pass
    
    #TODO
    def display_earth_feature(self):
        pass
    
    #TODO
    def display_earth(self):
        pass

    #TODO
    def display_asteroid_features(self):
        menu = ["You have selected the Asteroid feature !",
                "Once you have entered a date a graph representing the asteroids near Earth will be displayed"]
        self.display_menu(menu, True)
        
        number_of_try = 5
        
        while number_of_try > 0:
            date_string = self.get_user_input("Please enter a date with a valid format (YYYY-MM-DD) :\n")
            try:
                date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
                self.display_asteroid(date)
                break
            except:
                number_of_try -= 1
        else:
            self.display_menu(["Too many attempts",
                               "Disconnecting user {}".format(self.logged_user.username),
                               "Application stopping"])
            return
    
    def display_asteroid(self, date):
        graph = self.dao.get_graph(date)
        if graph == None:
            parameters = {
                'start_date': date.strftime("%Y-%m-%d"),
                'end_date': (date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            }
            data = self.fetch_data(self.api_queries['asteroid'], parameters)
            if data != None:
                self.dao.store_graph(date, data)
            else:
                self.display_menu(["No data for the entered date",
                                   "Application stopping"], True)
                return
        
        graph_points = self.dao.get_graph_points(date)
        increment = 360.0 / len(graph_points)
        graph = {
            'x': [0],
            'y': [0],
            'd': [1000]
        }
        
        for index, point in enumerate(graph_points):
            graph['x'].append(math.cos(increment * index) * (point.distance / 100000))
            graph['y'].append(math.sin(increment * index) * (point.distance / 100000))
            graph['d'].append(point.radius * 100)
        
        plt.figure()
        plt.scatter(graph['x'], graph['y'], graph['d'])
        plt.text(50, 50, "Earth", fontsize=14)
        plt.show()

if __name__ == "__main__":
    database_name = "database.db"
    application = Sakado(database_name, database_path=os.path.abspath(os.path.dirname(__file__)))
    application.display_login_screen()
