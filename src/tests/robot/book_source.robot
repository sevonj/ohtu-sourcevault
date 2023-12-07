*** Settings ***
Resource  resource.robot
Test Setup  Clear

# käyttäjä pystyy lisätä kirja-viitteitä appiin

*** Test Cases ***
Add Book Source With Valid Information
    Create Source
    Run
    Output Should Contain  Reference added
