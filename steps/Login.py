import behave


@behave.given('User navigates to 9gag login website')
def user_navigates_to_website(context):
    context.page.getPage()


@behave.when('User closes the pop up message')
def user_closes_the_pop_up_message(context):
    context.page.closePopUp()


@behave.when('User enters a username: "{username}"')
def user_enters_a_username(context, username):
    context.page.putUsername(username)


@behave.when('User enters a password: "{password}"')
def user_enters_a_password(context, password):
    context.page.putPassword(password)


@behave.when("User clicks on the login button")
def user_clicks_on_the_login_button(context):
    context.page.clickLogin()


@behave.then("User should be taken to successful login page")
def user_should_be_taken_to_successful_login_page(context):
    assert context.page.successfulPage() is True


@behave.then("User should be taken to unsuccessful login page")
def user_should_be_taken_to_unsuccessful_login_page(context):
    assert context.page.unsuccessfulPage() is True
