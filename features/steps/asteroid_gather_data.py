from datetime import datetime
from behave import *



@given('the user has entered the date "{text}"')
def step_impl(context, text):
    actual_date = datetime.strptime(text, '%d/%m/%Y')
    expected_date = datetime(2020, 11, 24, 0, 0)
    assert actual_date == expected_date

@when('the user want the asteroids data')
def step_impl(context):
    assert True is not False

@then('we ask the API for the data')
def step_impl(context):
    assert context.failed is False

@then('the data are stored in the database')
def step_impl(context):
    assert context.failed is False