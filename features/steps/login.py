#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import os
import sys

from behave import *

src_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\src")
sys.path.append(src_abs_path)
import model.user as user



@given('the user is logged in')
def step_impl(context):
    context.username = "Bernard123"
    context.password = "Tanpis321"
    context.user = user.User.create(username=context.username, password=context.password)
    context.disposable.append(context.user)

#SCENARIO: A user try to log in
@given('the user has an account registered')
def step_impl(context):
    context.username = "Bernard123"
    context.password = "Tanpis321"
    context.user = user.User.create(username=context.username, password=context.password)
    context.disposable.append(context.user)

@when('the user logs in with his valid credentials')
def step_impl(context):
    context.result_credentials = context.application.dao.verify_user_credentials(context.username, context.password)
    if context.result_credentials == True:
        context.application.logged_user = context.user
        context.failure = False
    else:
        context.failure = True

@then('the user is logged in')
def step_impl(context):
    assert context.application.logged_user == context.user
    assert context.failure is False

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