Feature: user registration

    Scenario: Successful sign up
        Given The user choose to sign up
        When The user writes a correct username
        And The user write a correct password
        Then the user account is created
        And a confirmation message is displayed

    Scenario: Duplicate username
        Given The user choose to sign up
        When The user writes a username that has already regestired
        Then an error message is displayed