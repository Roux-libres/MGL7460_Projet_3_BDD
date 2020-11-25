Feature: Manage favorites Nasa Astrology Picture Of the Day - APOD

    Scenario: add APOD to favorites
        Given the user is logged in
        And the APOD has been get
        When the user add the APOD to favorites
        Then the APOD is added to favorites

    Scenario: list favorites APOD
        Given the user is logged in
        When the user asks to see his favorites APOD
        Then user's favorites APOD names are listed

    Scenario: remove a APOD from favorites
        Given the user is logged in
        And the user's favorites APOD are listed
        When the user select and remove an APOD from his favorites
        Then the APOD is removed from the favorites list

    Scenario: display a favorite APOD in web browser
        Given the user is logged in
        And the user's favorites APOD are listed
        When the user choose one APOD to display
        Then the APOD opens in web browser
    
    Scenario: open favorites APOD page in web browser
        Given the user is logged in
        And the user's favorites APOD are listed
        When the user choose to display all his favorites APOD
        Then a page displaying all APOD and their names opens in web browser
