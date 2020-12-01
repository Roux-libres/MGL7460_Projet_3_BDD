#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import io
import json
import sys
import os

from behave import *

src_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\..\src")
sys.path.append(src_abs_path)
import model.favoriteapod

#Given('the user is logged in')

@when('the user asks to see the APOD')
def step_impl(context):
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock    
    
    context.apod = model.favoriteapod.FavoriteAPOD()
    context.apod.name = "Cygnus Without Stars"
    context.apod.date = "2020-11-30"
    context.apod.url = "https://apod.nasa.gov/apod/image/2011/CygnusStarless_Cameron_8859.jpg"
    
@then('the name of the APOD is displayed')
def step_impl(context):
    context.application.display_APOD(context.apod)
    output = context.stdout_mock.getvalue()
    assert context.apod.name == output
    
@then('the APOD is displayed in web browser')
def step_impl(context):
    pass
    
    sys.stdout = context.real_stdout
    