#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import json

from behave import *

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\..\src"))
import sakado

#Given('the user is logged in')

@when('the user asks to see the APOD')
def step_impl(context):
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock    
    
    url = context.application.queries["apod"]
    parameters = {"api_key" : context.application.api_key}
    context.apod = FavoriteAPOD()
    context.apod.user_id = context.application.logged_user.id
    context.apod.name = "Cygnus Without Stars"
    context.apod.date = "2020-11-30"
    context.apod.url = "https://apod.nasa.gov/apod/image/2011/CygnusStarless_Cameron_8859.jpg"
    
@then('the name of the APOD is displayed')
def step_impl(context):
    context.application.display_APOD(context.apod)
    assert context.failed is False
    
@then('the APOD is displayed in web browser')
def step_impl(context):
    assert context.failed is False
    
    sys.stdout = context.real_stdout
    