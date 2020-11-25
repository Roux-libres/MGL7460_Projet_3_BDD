Feature: Display earth image in the web browser
    Description
    Advanced description

    Background: A user need to be connected
        Given the user is logged in

    Scenario: Display Earth image from coordinates
        Given the user wants the Earth image of a location
         When the user types valid coordinates
         Then the image of the location is displayed on the web browser