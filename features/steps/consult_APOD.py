#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import io
import json
import os
import sys
import webbrowser

from behave import *

src_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\..\src")
sys.path.append(src_abs_path)
import model.favoriteapod



#Given('the user is logged in')

@when('the user asks to see the APOD')
def step_impl(context):    
    url = context.application.api_queries["apod"]
    context.apod_json = context.application.fetch_data(url, {})
    assert context.apod_json != None
    assert "error" not in context.apod_json
    
@then('the name of the APOD is displayed')
def step_impl(context):
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock
    
    context.application.display_APOD_in_prompt(context.apod_json)
    
    output = context.stdout_mock.getvalue()
    sys.stdout = context.real_stdout
    assert context.apod_json["title"] in output
    
@then('the APOD is displayed in web browser')
def step_impl(context):
    context.result_open = context.application.display_APOD_in_browser(context.apod_json)
    assert context.result_open is True
