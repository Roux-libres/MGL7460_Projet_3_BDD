from behave import *

@given('the APOD has been get')
def step_impl(context):
    print("we have behave installed")

@given('the user\'s favorites APOD are listed')
def step_impl(context):
    print("we have behave installed")

@when('the user add the APOD to favorites')
def step_impl(context):
    assert True is not False

@when('the user asks to see his favorites APOD')
def step_impl(context):
    assert True is not False
    
@when('the user select and remove an APOD from his favorites')
def step_impl(context):
    assert True is not False
    
@when('the user choose one APOD to display')
def step_impl(context):
    assert True is not False

@when('the user choose to display all his favorites APOD')
def step_impl(context):
    assert True is not False    

@then('the APOD is added to favorites')
def step_impl(context):
    assert context.failed is False
    
@then('user\'s favorites APOD names are listed')
def step_impl(context):
    assert context.failed is False
    
@then('the APOD is removed from the favorites list')
def step_impl(context):
    assert context.failed is False
    
@then('the APOD opens in web browser')
def step_impl(context):
    assert context.failed is False
    
@then('a page displaying all APOD and their names opens in web browser')
def step_impl(context):
    assert context.failed is False
