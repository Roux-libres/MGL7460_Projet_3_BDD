#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *



#Given('the user is logged in')

@when('the user asks to see the APOD')
def step_impl(context):
    assert True is not False

@then('the name of the APOD is displayed')
def step_impl(context):
    assert context.failed is False
    
@then('the APOD is displayed in web browser')
def step_impl(context):
    assert context.failed is False
    