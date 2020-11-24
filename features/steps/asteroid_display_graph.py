from behave import *



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