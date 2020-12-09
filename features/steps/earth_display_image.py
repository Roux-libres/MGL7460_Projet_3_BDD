#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *
import webbrowser

#SCENARIO: A user wants a 2D graph to be displayed
@given('the user wants the Earth image of a location')
def step_impl(context):
    print('the user wants the Earth image of a location')

@when('the user types valid coordinates')
def step_impl(context):
    context.longitude = -95.33
    context.latitude = 29.78    
    context.dimension = 0.4
    
    parameters = {
        'lon': context.longitude, 
        'lat': context.latitude,
        'dim': context.dimension,
        'date': "2018-01-01"
    }
    
    result = context.application.fetch_data(url=context.application.api_queries['earth'], parameters=parameters)
    assert result != None
    context.earth_url = result['url']

@then('the image of the location is displayed on the web browser')
def step_impl(context):
    try:
        context.application.open_url_in_browser(context.earth_url)
        context.failure = False
    except webbrowser.Error as error:
        print("Error during opening of url\nError : {}".format(error))
        context.failure = True
    assert context.failure is False 