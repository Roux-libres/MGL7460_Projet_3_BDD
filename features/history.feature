Feature: History of user queries

    Scenario: A user wants their last five queries to be displayed
        Given the user is logged in
        And the user wants his request history
        When the history is not empty
        Then the history of the last five user queries is displayed
