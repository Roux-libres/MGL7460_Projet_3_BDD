#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

from behave import *
import io
import os
import sys



#SCENARIO: A user wants their last five queries to be displayed

#Given('the user is logged in')

@when('the user wants his request history')
def step_impl(context):
    context.number_of_query = 5
    context.queries = []
    for index in range(context.number_of_query):
        context.queries.append(context.application.dao.store_query(user_id=context.user.id, content="Query number {}".format(index)))
        context.disposable.append(context.application.dao.store_query(user_id=context.user.id, content="Query number {}".format(index)))

@then('the history of the last five user queries is displayed')
def step_impl(context):
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock
    
    context.application.display_queries_in_prompt(context.queries)

    output = context.stdout_mock.getvalue()
    sys.stdout = context.real_stdout

    if (len(context.queries) > 0):
        for query in context.queries:
            assert query.content in output
    else:
        assert "You haven't old queries" in output
