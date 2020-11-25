#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *



#SCENARIO: A user try to log in
@given('the user has an account registered')
def step_impl(context):
    context.username = "Bernard123"
    context.password = "Tanpis321"
    #START TRANSACTION
    context.user = User(username=context.username, password=context.password)
    context.user.save()

@when('the user logs in with his valid credentials')
def step_impl(context):
    context.user.log_in(context.username, context.password)

@then('the user is logged in')
def step_impl(context):
    assert context.user != None
    #ROLLBACK TRANSACTION

#SCENARIO: A user try to log in but he has no account
@given('the user has no account registered')
def step_impl(context):
    pass

@when('the user logs in with unknown credentials')
def step_impl(context):
    pass

@then('the user is asked to register an account')
def step_impl(context):
    pass

#SCENARIO: A user try to log with invalid password

#STEP: the user has an account registered

@when('the user logs in with invalid password')
def step_impl(context):
    pass

@then('the user is told to enter a valid password')
def step_impl(context):
    pass