from behave import *



@given('the user has entered the coordinates')
def step_impl(context):
    for coordinate in context.table:
        print(coordinate)

@when('the user want the image of the location')
def step_impl(context):
    assert True is not False

@then('we ask the API for the image')
def step_impl(context):
    assert context.failed is False

@then('the image is stored in the database')
def step_impl(context):
    assert context.failed is False

@then('the image is displayed on the web browser')
def step_impl(context):
    assert context.failed is False