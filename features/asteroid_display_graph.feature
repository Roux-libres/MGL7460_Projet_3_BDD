Feature: Display 2D graph representing the asteroids near earth
    Description
    Advanced description

    Background: A user needs to be connected
        Given the user is logged in

    Scenario: A user wants a 2D graph to be displayed
        Given the user wants a graph of the asteroids data
         When the user types a valid date
         Then the graph is displayed