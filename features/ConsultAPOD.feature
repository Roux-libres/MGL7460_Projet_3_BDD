Feature: Consult the Nasa Astrology Picture Of the Day (APOD)

    Scenario: get nasa apod
        Given the user is logged in
        When the user asks to see the APOD
        Then the name of the APOD is displayed in prompt
        And the APOD is displayed in web browser
