Feature: use the Asteroid NASA's API
    The Asteroid NASA's API is used to gather and display the asteroids near the Earth.
    The data gathered can be stored in the database. 

    Scenario: gather asteroids data for a specific date
        Given the Asteroid NASA API is reachable
          And the user is logged in
          And the user has entered a valid date
         When user want the asteroids data
         Then we ask the API for the data
          And the data are stored in the database

    Scenario: display 2D graph representing the Earth and near asteroids
        Given the user is logged in
          And the data has been stored in the database
         When the user ask to display the graph
         Then we will recover the data
          And we will generate the graph
          And we will display the graph
