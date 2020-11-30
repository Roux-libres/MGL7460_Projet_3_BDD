Feature: Manage favorites Nasa Astrology Picture Of the Day - APOD

    Background: A user needs to be connected
        Given the user is logged in

    Scenario: A user adds the APOD to his favorites
        Given the APOD has been fetched
         When the user chooses to add the APOD to favorites
         Then the APOD is added to favorites

    Scenario: A user lists favorites APOD
         When the user asks to see his favorites APOD
         Then user's favorites APOD names are listed

    Scenario: A user remove a APOD from favorites
        Given the user has favorites APOD
         When the user selects and chooses to remove an APOD from his favorites
         Then the APOD is removed from the favorites list

    Scenario: Display a user's favorite APOD in web browser
        Given the user has favorites APOD
         When the user chooses one APOD to display
         Then the APOD opens in web browser
    
    Scenario: Open a user's favorites APOD page in web browser
        Given the user has favorites APOD
         When the user chooses to display all his favorites APOD
         Then a page displaying all APOD and their names opens in web browser
