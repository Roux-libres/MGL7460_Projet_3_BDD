#pylint: disable=undefined-variable
#pylint: disable=function-redefined
#pylint: disable=unused-wildcard-import

import os
import sys
import io

from behave import *



#SCENARIO: A user adds the APOD to his favorites
@given('the APOD has been fetched')
def step_impl(context):
    context.apod_json = {
        "date": "2020-12-01",
        "explanation": "Are stars still forming in the Milky Way's satellite galaxies?  Found among the Small Magellanic Cloud's (SMC's) clusters and nebulas, NGC 346 is a star forming region about 200 light-years across, pictured here in the center of a Hubble Space Telescope image. A satellite galaxy of the Milky Way, the Small Magellanic Cloud (SMC) is a wonder of the southern sky, a mere 210,000 light-years distant in the constellation of the Toucan (Tucana). Exploring NGC 346, astronomers have identified a population of embryonic stars strung along the dark, intersecting dust lanes visible here on the right. Still collapsing within their natal clouds, the stellar infants' light is reddened by the intervening dust. Toward the top of the frame is another star cluster with intrinsically older and redder stars. A small, irregular galaxy, the SMC itself represents a type of galaxy more common in the early Universe. These small galaxies, though, are thought to be building blocks for the larger galaxies present today.   All 30: 2020 November APODs voiced by AI",
        "hdurl": "https://apod.nasa.gov/apod/image/2012/Ngc346_HubbleSchmidt_3375.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Test",
        "url": "https://apod.nasa.gov/apod/image/2012/Ngc346_HubbleSchmidt_960.jpg"
    }

@when('the user chooses to add the APOD to favorites')
def step_impl(context):
    pass

@then('the APOD is added to favorites')
def step_impl(context): 
    context.favorite_apod = context.application.dao.store_favorite_apod(context.user, context.apod_json)
    context.disposable.append(context.favorite_apod)
    assert context.favorite_apod != None

#SCENARIO: A user lists favorites APOD
@when('the user asks to see his favorites APOD')
def step_impl(context):
    context.favorites_apod = context.application.dao.get_favorites_apod(context.user)

@then("user's favorites APOD names are listed")
def step_impl(context):
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock

    context.application.display_favorites_APOD(context.favorites_apod)

    output = context.stdout_mock.getvalue()
    sys.stdout = context.real_stdout
    
    for favorite_apod in context.favorites_apod:
        assert favorite_apod.title in output

#SCENARIO: A user remove a APOD from favorites
@given('the user has favorites APOD')
def step_impl(context):
    context.apod_json = {
        "date": "2020-12-01",
        "explanation": "Are stars still forming in the Milky Way's satellite galaxies?  Found among the Small Magellanic Cloud's (SMC's) clusters and nebulas, NGC 346 is a star forming region about 200 light-years across, pictured here in the center of a Hubble Space Telescope image. A satellite galaxy of the Milky Way, the Small Magellanic Cloud (SMC) is a wonder of the southern sky, a mere 210,000 light-years distant in the constellation of the Toucan (Tucana). Exploring NGC 346, astronomers have identified a population of embryonic stars strung along the dark, intersecting dust lanes visible here on the right. Still collapsing within their natal clouds, the stellar infants' light is reddened by the intervening dust. Toward the top of the frame is another star cluster with intrinsically older and redder stars. A small, irregular galaxy, the SMC itself represents a type of galaxy more common in the early Universe. These small galaxies, though, are thought to be building blocks for the larger galaxies present today.   All 30: 2020 November APODs voiced by AI",
        "hdurl": "https://apod.nasa.gov/apod/image/2012/Ngc346_HubbleSchmidt_3375.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "Test",
        "url": "https://apod.nasa.gov/apod/image/2012/Ngc346_HubbleSchmidt_960.jpg"
    }

    context.favorite_apod = context.application.dao.store_favorite_apod(context.user, context.apod_json)
    context.disposable.append(context.favorite_apod)
    
@when('the user selects and chooses to remove an APOD from his favorites')
def step_impl(context):
    pass

@then('the APOD is removed from the favorites list')
def step_impl(context):
    result_delete = context.application.dao.remove_favorite_apod(context.favorite_apod)
    assert result_delete is True
