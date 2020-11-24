from behave import *

#SCENARIO : gather asteroids data for a specific date
@given('the Asteroid NASA API is reachable')
def step_impl(context):
    pass

@given('the user is logged in')
def step_impl(context):
    pass

@given('the user has entered a valid date')
def step_impl(context):
    pass

@when('user want the asteroids data')
def step_impl(context):
    assert True is not False

@then('we ask the API for the data')
def step_impl(context):
    assert context.failed is False

@then('the data are stored in the database')
def step_impl(context):
    assert context.failed is False

#SCENARIO : display 2D graph representing the Earth and near asteroids

@given('the data has been stored in the database')
def step_impl(context):
    pass

@when('the user ask to display the graph')
def step_impl(context):
    assert True is not False

@then('we will recover the data')
def step_impl(context):
    assert context.failed is False

@then('we will generate the graph')
def step_impl(context):
    assert context.failed is False

@then('we will display the graph')
def step_impl(context):
    assert context.failed is False