Feature: History of user queries

    Scenario: Save the last user queries
        Given the user is logged in
        When the user makes a request
        Then the query is added to the history.

    Scenario: Display the last five user queries
        Given the user is logged in
        When the user asks to see his request history
        And the history is not empty
        Then the history of the last five user queries is displayed

    Scenario: Run a query in the history 
        Given the user is logged in
        And the history of the last five user queries is displayed
        When the user selects one query
        And the user asks to run selected query
        Then the query is runned 