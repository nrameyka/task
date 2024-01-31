	Write a simple automated test case using Selenium and PyTest.
 
	- Page to test: https://www.browserstack.com/users/sign_in
	- Scenario (negative): Login attempt with invalid e-mail format:
		- Open page
		- Enter email in invalid format into email field- test_user
		- Enter password into password - 12345678
		- Click “Sign me in” button
		- Check that “Invalid Email” message appears in email field
		- Check that URL path of the page is still “/users/sign_in”
	- Credentials must be read from a file: credentials.yaml or credentials.json
	- (Optional) Usage of PyTest fixtures for setup/teardown is encouraged
	- (Optional) Provide base URL as a CLI option to pytest
	(pytest --base_page_url https://www.browserstack.com)