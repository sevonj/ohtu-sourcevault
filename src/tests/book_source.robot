*** Settings ***
Resource  resource.robot
Test Setup  Clear

*** Test Cases ***
Add Book Source With Valid Information
    Create Source
    Run
    Output Should Contain  Reference added
