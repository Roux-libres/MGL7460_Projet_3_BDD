#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import datetime

from behave import *



#SCENARIO: A user wants a 2D graph to be displayed
@given('the user wants a graph of the asteroids data')
def step_impl(context):
    pass

@when('the user types a valid date')
def step_impl(context):
    context.date_format = '%Y-%m-%d'
    context.date_string = "2015-09-07"
    try:
        context.date = datetime.datetime.strptime(context.date_string, context.date_format) + datetime.timedelta(days=1)
        context.failure = False
    except ValueError:
        print("Invalid date")
        context.failure = True
    assert context.failure is False

@then('the graph is displayed')
def step_impl(context):
    result = context.application.display_asteroid(context.date)
    assert result is True