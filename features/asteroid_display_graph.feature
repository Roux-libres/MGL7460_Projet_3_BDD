Feature: display graph representing the asteroids near earth
    Description
    Advanced description

    Scenario: display 2D graph representing the Earth and near asteroids
        Given the user is logged in
          And the data has been stored in the database
         When the user ask to display the graph
         Then we will recover the data
          And we will generate the graph
          And we will display the graph