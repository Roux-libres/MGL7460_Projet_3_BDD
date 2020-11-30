#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import os
import sys

from behave import *

src_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\..\src")
sys.path.append(src_abs_path)
import sakado



@given('the user is logged in')
def step_impl(context):
    context.application = sakado.Sakado("database.db", database_path=src_abs_path)
    context.application.dao
    

#SCENARIO: A user try to log in
@given('the user has an account registered')
def step_impl(context):
    """
    context.username = "Bernard123"
    context.password = "Tanpis321"
    #START TRANSACTION
    context.user = User(username=context.username, password=context.password)
    context.user.save()
    """
    pass

@when('the user logs in with his valid credentials')
def step_impl(context):
    #context.user.log_in(context.username, context.password)
    pass

@then('the user is logged in')
def step_impl(context):
    #assert context.user != None
    #ROLLBACK TRANSACTION
    pass

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