#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import webbrowser

from behave import *



#SCENARIO: A user wants a 2D graph to be displayed
@given('the user wants the Earth image of a location')
def step_impl(context):
    print('the user wants the Earth image of a location')

@when('the user types valid coordinates')
def step_impl(context):
    context.longitude = 45.512561
    context.latitude = -73.560608
    context.dimension = 0.5
    
    parameters = {
        'api_key' : "DEMO_KEY",
        'lon': context.longitude, 
        'lat': context.latitude,
        'dim': context.dimension
    }
    
    result = context.application.fetch_data(url=context.application.api_queries['earth'], parameters=parameters)
    assert result != None
    context.earth_url = result['url']

@then('the image of the location is displayed on the web browser')
def step_impl(context):
    try:
        webbrowser.open(context.earth_url)
    except webbrowser.Error as error:
        print("Error during opening of url\nError : {}".format(error))
    assert context.failure is False