Feature: History of user queries

    Scenario: A user wants to see their last five queries
        Given the user is logged in
        When the user asks to see his request history
        And the history is not empty
        Then the history of the last five user queries is displayed
