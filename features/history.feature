Feature: History of user queries

    Scenario: A user wants their last five queries to be displayed
        Given the user is logged in
        When the user wants his request history
        Then the history of the last five user queries is displayed
