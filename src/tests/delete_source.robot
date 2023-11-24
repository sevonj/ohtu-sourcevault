*** Settings ***
Resource  resource.robot
Test Setup  Clear

*** Test Cases ***
Delete Existing Source
    Create Source
    Input Command  6
    Input Command  Kirjailija23
    Run
    Output Should Contain  Citation removed succesfully.

Delete NonExisting Source
    Input Command  6
    Input Command  Avain123
    Run
    Output Should Contain  No such citation.
