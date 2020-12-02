#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *



#SCENARIO: A user successfuly sign up

#given('the user has no account registered')

@when('the user sign up with valid credentials')
def step_impl(context):
    context.user = context.application.dao.store_user(username=context.username, password=context.password)
    context.disposable.append(context.user)

@then('the user account is created')
def step_impl(context):
    assert context.user == context.application.dao.verify_user_credentials(username=context.username, password=context.password)

#SCENARIO: A user try to sign up but username is already taken

#given('the user has no account registered')

@when('the user sign up with an already taken username')
def step_impl(context):
    context.disposable.append(context.application.dao.store_user(username=context.username, password=context.password))
    context.user = context.application.dao.store_user(username=context.username, password=context.password)
    context.disposable.append(context.user)

@then('the user is told to choose another username')
def step_impl(context):
    assert context.user == None
    context.application.display_menu(["Username already taken", "Please enter another username"])
