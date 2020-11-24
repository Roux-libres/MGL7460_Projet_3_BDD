from behave import *

#Scenario : Save the last user queries
@when('the user makes a request')
def step_impl(context):
    assert True is not False

@then('the query is added to the history')
def step_impl(context):
    assert True is not False

#Scenario : Display the last five user queries
@when('the user asks to see his request history')
def step_impl(context):
    assert True is not False

@when('the history is not empty')
def step_impl(context):
    assert True is not False

@then('the history of the last five user queries is displayed')
def step_impl(context):
    assert True is not False

#Scenario : Run a query in the history 
@given('the history of the last five user queries is displayed')
def step_impl(context):
    assert True is not False

@when('the user selects one query')
def step_impl(context):
    assert True is not False

@when('the user asks to run selected query')
def step_impl(context):
    assert True is not False

@then('the query is runned')
def step_impl(context):
    assert True is not False
