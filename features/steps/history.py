#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *



#SCENARIO: A user wants their last five queries to be displayed

#Given('the user is logged in')

@when('the user wants his request history')
def step_impl(context):
    context.number_of_query = 5

@then('the history of the last five user queries is displayed')
def step_impl(context):
    context.application.display_queries()
    assert len(context.application.dao.get_query_from_user(user=context.user, limit=context.number_of_query))
