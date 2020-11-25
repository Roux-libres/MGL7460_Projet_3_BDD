Feature: gather data from the NASA API
    Description
    Advanced description

    Scenario: gather asteroids data for a specific date
        Given the user is logged in
          And the user has entered the date "24/11/2020"
         When the user want the asteroids data
         Then we ask the API for the data
          And the data are stored in the database