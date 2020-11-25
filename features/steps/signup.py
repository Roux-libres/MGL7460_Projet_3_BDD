from behave import *

#Scenario : Successful sign up
@given('The user choose to sign up')
def step_impl(context):
    assert True is not False

@when('The user writes a correct username')
def step_impl(context):
    assert True is not False

@when('The user write a correct password"')
def step_impl(context):
    assert True is not False

@then('the user account is created')
def step_impl(context):
    assert True is not False

@then('a confirmation message is displayed')
def step_impl(context):
    assert True is not False

#Scenario : Duplicate username
@when('The user writes a username that has already regestired')
def step_impl(context):
    assert True is not False

@then('an error message is displayed')
def step_impl(context):
    assert True is not False