*** Settings ***
Resource  resource.robot
Test Setup  Clear

*** Test Cases ***
List Correct Keys
    Create Source
    Input Command  4
    Input Command  8
    Run
    Output Should Contain  Kirjailija23
    Output Should Contain  There exists 1 citation keys:

List No Keys
    Input Command  4
    Input Command  8
    Run
    Output Should Contain  There exists 0 citation keys:
