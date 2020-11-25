Feature: User login

    Scenario: Sucessfull login
        Given a user account 
            | username  | password  |
            | Robert123 | azerty321 |

        When the user writes in username input "Robert123"
        And  
        Then the user is logged in