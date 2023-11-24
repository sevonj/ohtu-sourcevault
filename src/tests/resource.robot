*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Command
    [Arguments]  ${command}
    Input  ${command}

Input Information
    [Arguments]  ${data}
    Input  ${data}
