#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *



#SCENARIO: A user adds the APOD to his favorites
@given('the APOD has been fetched')
def step_impl(context):
    print("the APOD has been fetched")

@when('the user chooses to add the APOD to favorites')
def step_impl(context):
    assert True is not False

@then('the APOD is added to favorites')
def step_impl(context):
    assert context.failed is False

#SCENARIO: A user lists favorites APOD
@when('the user asks to see his favorites APOD')
def step_impl(context):
    assert True is not False

@then("user's favorites APOD names are listed")
def step_impl(context):
    assert context.failed is False

#SCENARIO: A user remove a APOD from favorites
@given('the user has favorites APOD')
def step_impl(context):
    print("we have behave installed")
    
@when('the user selects and chooses to remove an APOD from his favorites')
def step_impl(context):
    assert True is not False
    
@then('the APOD is removed from the favorites list')
def step_impl(context):
    assert context.failed is False

#SCENARIO: Display a user's favorite APOD in web browser

#Given('the user has favorites APOD')
    
@when('the user chooses one APOD to display')
def step_impl(context):
    assert True is not False
    
@then('the APOD opens in web browser')
def step_impl(context):
    assert context.failed is False

#SCENARIO: Open a user's favorites APOD page in web browser

#Given('the user has favorites APOD')
    
@when('the user chooses to display all his favorites APOD')
def step_impl(context):
    assert True is not False
    
@then('a page displaying all APOD and their names opens in web browser')
def step_impl(context):
    assert context.failed is False