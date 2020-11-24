Feature: display Earth image from coordinates using NASA API
    Description
    Advanced description

    Scenario: display Earth image from coordinates
        Given the user is logged in
          And the user has entered the coordinates
            | "45.512463" |
            | "-73.560542" |
         When the user want the image of the location
         Then we ask the API for the image
          And the image is stored in the database
          And the image is displayed on the web browser