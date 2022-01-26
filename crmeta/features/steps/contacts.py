from behave import given, when, then


@given('we have a new contact')
def step_impl(context):
    pass


@when('we add the new contact')
def step_impl(context):
    assert True is not False


@then('crmeta will allow us to add that contact!')
def step_impl(context):
    assert context.failed is False
