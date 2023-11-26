*** Settings ***
Library  ../app_library.py

*** Keywords ***
Input Command
    [Arguments]  ${command}
    Input  ${command}

Create Source
    Input Command  1
    Input Command  1
    Input Command  Kirjailija
    Input Command  Otsikko
    Input Command  2023
    Input Command  Julkaisija
    Input Command  q

Run
    Input Command  8
    Run Application
