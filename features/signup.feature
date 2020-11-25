Feature: User registration

    Scenario: A user successfuly sign up
        Given the user has no account registered
         When the user sign up with valid credentials
         Then the user account is created

    Scenario: A user try to sign up but username is already taken
        Given the user has no account registered
         When the user sign up with an already taken username
         Then the user is told to choose another username