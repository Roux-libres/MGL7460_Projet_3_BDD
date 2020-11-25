Feature: User try to log in

    Scenario: A user try to log in
        Given the user has an account registered
         When the user logs in with his valid credentials
         Then the user is logged in

    Scenario: A user try to log in but he has no account
        Given the user has no account registered
         When the user logs in with unknown credentials
         Then the user is asked to register an account

    Scenario: A user try to log with invalid password
        Given the user has an account registered
         When the user logs in with invalid password
         Then the user is told to enter a valid password