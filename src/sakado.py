import datetime
import json
import math
import os
import requests
import sys
import time
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
            "earth"     : "https://api.nasa.gov/planetary/earth/assets?"
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
        queries = self.dao.get_queries_from_user(self.logged_user)
        if len(queries) != 0 :
            queries_list = [str(i) + " : " + query.content for i, query in enumerate(queries)]
            menu = ["There is the list of your old queries :"]
            menu.extend(queries_list)
            self.display_menu(menu, True)
        else:
            self.display_menu(["You haven't old queries"], True)
        self.get_user_input("Return to previous menu (enter)")
      
    def fetch_data(self, url, parameters):
        try:
            url += 'api_key=' + self.api_key
            for parameter in parameters:
                url += '&' + parameter + '=' + str(parameters[parameter])
            self.dao.store_query(self.logged_user.id, url)
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
    
    def display_APOD_features(self):
        main_menu = ["You have selected the Astronomy Picture of the Day (APOD) feature !",
                "Please choose one of the following functionality :",
                "1) Display the APOD",
                "2) Display your favorites APOD (in your browser)",
                "3) Remove some APOD from you favorites",
                "4) Return to main menu"]
        
        while True:
            self.display_menu(main_menu, True)
            choice = self.get_user_input("Please enter a number associated with a functionality : ")
            
            if choice == "1":
                self.display_APOD(self.fetch_data(self.api_queries["apod"], {}))
            elif choice == "2":
                self.manage_display_favorites_APOD()
            elif choice == "3":
                self.remove_favorites_APOD()
            elif choice == "4":
                #TODO
                break
            else:
                print("Invalid choice")
            self.get_user_input("Return to previous menu (enter)")

    def display_APOD(self, apod_json):
        print("APOD title :", apod_json["title"])
        self.open_url_in_browser(apod_json["hdurl"])
        
        while True:
            choice = self.get_user_input("Do you want to add the APOD to your favorites ? (y/n) : ")
            
            if choice == "y":
                self.dao.store_favorite_apod(self.logged_user, apod_json)
                break
            elif choice == "n":
                break
            else:
                print("Invalide choice (y or n)")
      
    def display_favorites_APOD(self, fav_apods):        
        if len(fav_apods) != 0 :
            fav_apods_names = [str(i) + " : " + apod.name for i, apod in enumerate(fav_apods)]
            menu = ["There is the list of your favorites APOD :"]
            menu.extend(fav_apods_names)
            self.display_menu(menu, True)
        else:
            self.display_menu(["You haven't any favorite APOD"], True)
    
    def manage_display_favorites_APOD(self):        
        favs_apods = self.dao.get_favorites_apod(self.logged_user)
        if len(favs_apods) != 0 :
            while True:
                self.display_favorites_APOD(favs_apods)
            
                try:
                    apod_id = self.get_user_input("Which one do you want to display ? (enter its number or nothing to go back to previous menu) : ")
                    
                    if apod_id == "":
                        break
                    else:
                        apod_id = int(apod_id)
                        
                    if apod_id in range(len(favs_apods)):
                        self.open_url_in_browser(favs_apods[apod_id].url)
         
                except ValueError:
                    self.get_user_input("Invalide choice")             
        else:
            self.display_menu(["You haven't any favorite APOD"], True)

    def remove_favorites_APOD(self):
        while True:
            favs_apods = self.dao.get_favorites_apod(self.logged_user)
            self.display_favorites_APOD(favs_apods)
        
            try:
                apod_id = self.get_user_input("Which one do you want to remove ? (enter its number or nothing to go back to previous menu) : ")
                
                if apod_id == "":
                    break
                else:
                    apod_id = int(apod_id)
                    
                if apod_id in range(len(favs_apods)):
                    if self.get_user_input("Are you sure you want to remove the APOD number {0} ? (y or n) : ".format(apod_id)) == "y":
                        self.dao.remove_favorite_apod(favs_apods[apod_id])
                        self.get_user_input("The APOD number {0} has been removed".format(apod_id))
                else:
                    self.get_user_input("Invalide choice")              
            except ValueError:
                self.get_user_input("Invalide choice")                   
    
    def display_earth_feature(self):
        main_menu = ["You have selected the Earth feature !",
        "Please choose one of the following functionality :",
        "1) Display a satellite image of the earth with specific coordinates",
        "2) Return to main menu"]

        while True:
            self.display_menu(main_menu, True)
            choice = self.get_user_input("Please enter a number associated with a functionality : ")
            
            if choice == "1":
                self.display_earth()
            elif choice == "2":
                break
            else:
                print("Invalid choice")
            self.get_user_input("Return to previous menu (enter)")
    
    def check_float_to_input(self, message):
        input = self.get_user_input(message)
        while 1:
            try:
                input = float(input)
                break
            except:
                print("Please enter a correct float value.")
                input = self.get_user_input(message)
        return input       

    def display_earth(self):
        latitude = self.check_float_to_input("Enter the latitude (float value): ")
        longitude = self.check_float_to_input("Enter the longitude (float value): ")
        dimension = self.check_float_to_input("Enter the dimension - width and height of image in degrees - (float value): ")
        parameters = {
            'lat': latitude,
            'lon': longitude,
            'dim' : dimension,
            'date' : "2018-01-01"
        }
        data = self.fetch_data(self.api_queries["earth"], parameters)
        try:
            self.open_url_in_browser(data.url)
        except:
            print("No imagery for these coords.")

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
    
    def display_asteroid(self, date, close_after=0):
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
            'd': [2000]
        }
        
        for index, point in enumerate(graph_points):
            graph['x'].append(math.cos(increment * index) * (point.distance / 100000))
            graph['y'].append(math.sin(increment * index) * (point.distance / 100000))
            graph['d'].append(point.radius * 100)
        
        plt.figure(num="Asteroids near Earth", figsize=(6, 4.5))
        plt.scatter(graph['x'], graph['y'], graph['d'])
        plt.text(-85, -30, "Earth", fontsize=14)
        plt.text(350, 700, "Échelle 1:100000 km", fontsize=8)
        plt.xlim((-750, 750))
        plt.ylim((-750, 750))
        if close_after > 0: plt.ion()
        plt.show()
        
        if close_after > 0:
            plt.pause(.05)
            time.sleep(close_after)
            plt.close()
        
        return True

if __name__ == "__main__":
    database_name = "database.db"
    application = Sakado(database_name, database_path=os.path.abspath(os.path.dirname(__file__)))
    application.display_login_screen()
