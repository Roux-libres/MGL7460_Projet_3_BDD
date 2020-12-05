#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import os
import sys

from behave import *



@given('the user is logged in')
def step_impl(context):
    context.username = "Bernard123"
    context.password = "Tanpis321"
    context.user = context.application.dao.store_user(context.username, context.password)
    context.disposable.append(context.user)
    context.application.logged_user = context.user

#SCENARIO: A user try to log in
@given('the user has an account registered')
def step_impl(context):
    context.username = "Bernard123"
    context.password = "Tanpis321"
    context.user = context.application.dao.store_user(context.username, context.password)
    context.disposable.append(context.user)

@when('the user logs in with his valid credentials')
def step_impl(context):
    context.result_credentials = context.application.dao.verify_user_credentials(context.username, context.password)
    if context.result_credentials == context.user:
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
    context.username = "Tanpis321"
    context.password = "Bernard123"

@when('the user logs in with unknown credentials')
def step_impl(context):
    context.result_credentials = context.application.dao.verify_user_credentials(context.username, context.password)
    if not context.result_credentials:
        context.failure = False
    else:
        context.failure = True

@then('the user is asked to register an account')
def step_impl(context):
    assert context.failure is False
    context.application.display_menu(["There is no account using this username", "Please register a new account"])

#SCENARIO: A user try to log with invalid password

#STEP: the user has an account registered

@when('the user logs in with invalid password')
def step_impl(context):
    context.password = "123sipnaT"
    context.result_credentials = context.application.dao.verify_user_credentials(context.username, context.password)
    if context.result_credentials:
        context.failure = False
    else:
        context.failure = True

@then('the user is told to enter a valid password')
def step_impl(context):
    assert context.failure is False
    context.application.display_menu(["Incorrect password", "Please enter a valid password"])
    