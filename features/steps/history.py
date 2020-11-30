#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *



#SCENARIO: A user wants their last five queries to be displayed

#Given('the user is logged in')

@when('the user wants his request history')
def step_impl(context):
    assert True is not False

@then('the history of the last five user queries is displayed')
def step_impl(context):
    assert True is not False
