*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Book Source With Valid Information
    Input Command  1
    Input Command  1
    Input Information  Kirjailija
    Input Information  Otsikko
    Input Information  2023
    Input Information  Julkaisija
    Input Command  q
    Input Command  8
    Run Application
    Output Should Contain  Reference added
