Feature: Registration Page
    As a new moneygaming.com player
    I want to be able to register using my full details
    So that I can play online casino games


    Scenario: Login to the back office
        Given I am a new moneygaming.com player
        Given I navigate to 'HomePage'
        Given 'HomePage' page is loaded
        When I Click the JOIN NOW button to open the registration page
        Then 'Registration' page is loaded
        When I Select a title value from the dropdown
        When I Enter 'Taye' in the firstname field
        When I Enter 'Oyelekan' in the surname field
        When I Check the checkbox with text 'I accept the Terms and Conditions and certify that I am over the age of 18.'
        When I Submit the form by clicking the JOIN NOW button
        Then Validate that a validation message with text 'This field is required' appears under the date of birth box

