#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *



#SCENARIO: A user successfuly sign up

#given('the user has no account registered')

@when('the user sign up with valid credentials')
def step_impl(context):
    pass

@then('the user account is created')
def step_impl(context):
    pass

#SCENARIO: A user try to sign up but username is already taken

#given('the user has no account registered')

@when('the user sign up with an already taken username')
def step_impl(context):
    pass

@then('the user is told to choose another username')
def step_impl(context):
    pass