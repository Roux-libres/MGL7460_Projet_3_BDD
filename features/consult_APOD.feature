Feature: Consult the Nasa Astrology Picture Of the Day - APOD

    Scenario: A user want to consult the APOD
        Given the user is logged in
        When the user asks to see the APOD
        Then the name of the APOD is displayed
        And the APOD is displayed in web browser
