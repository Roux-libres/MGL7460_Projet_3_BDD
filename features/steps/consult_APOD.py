#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import io
import json
import sys
import os
import webbrowser

from behave import *

src_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\..\src")
sys.path.append(src_abs_path)
import model.favoriteapod

#Given('the user is logged in')

@when('the user asks to see the APOD')
def step_impl(context):    
    url = context.application.api_queries["apod"]
    data = context.application.fetch_data(url, {})
    context.apod = model.favoriteapod.FavoriteAPOD()
    context.apod.name = data.title
    context.apod.date = data.date
    context.apod.url = data.hdurl
    
@then('the name of the APOD is displayed')
def step_impl(context):
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock
    
    try:
        context.application.display_APOD(context.apod)
    except webbrowser.Error as error:
        print("Error during opening of url\nError : {}".format(error))
        context.failure = True
    
    output = context.stdout_mock.getvalue()
    sys.stdout = context.real_stdout
    assert context.apod.name == output
    
@then('the APOD is displayed in web browser')
def step_impl(context):
    assert context.failure is False
    