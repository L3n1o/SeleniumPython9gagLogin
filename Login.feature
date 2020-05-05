Feature: Login into 9gag account
		 Existing 9gag user should be able to login into an account by using correct credentails

Scenario Outline: Login into account with user data

	Given 	User navigates to 9gag login website
	When 	User closes the pop up message
	When 	User enters a username: "<username>"
	When 	User enters a password: "<password>"
	When 	User clicks on the login button
	Then 	User should be taken to unsuccessful login page


Examples: Bad data
|username			|password	|
|					|Example12@	|
|@gmail.com			|Example12@	|
|example			|Example12@	|
|example@gmail.com	|			|
|example@gmail.com	|Example12@	|

Examples: Good data
|username			|password	|
|example@gmail.com	|Example12@	|

