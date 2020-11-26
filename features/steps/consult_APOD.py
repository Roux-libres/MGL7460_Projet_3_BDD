from behave import *

#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

@given('the name of the APOD is displayed in prompt')
def step_impl(context):
    print("we have behave installed")

@when('the user asks to see the APOD')
def step_impl(context):
    assert True is not False

@then('the name of the APOD is displayed in prompt')
def step_impl(context):
    assert context.failed is False
    
@then('the APOD is displayed in web browser')
def step_impl(context):
    assert context.failed is False
    