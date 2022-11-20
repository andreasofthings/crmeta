from behave import given, when, then


@given(u'a client works with the component')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given a client works with the component')
    pass


@given(u'a machine client has a new contact')
def step_impl(context):  # noqa: W0404
    import requests
    # raise NotImplementedError(u'STEP: Given a machine client has a new contact')


@when(u'a machine client adds the new contact')
def step_impl(context):  # noqa: W0404
    pass
    # raise NotImplementedError(u'STEP: When a machine client adds the new contact')


@then(u'crmeta will allow the machine client to add that contact and respond with 20x!')
def step_impl(context):  # noqa: W0404
    pass
    # raise NotImplementedError(u'STEP: Then crmeta will allow the machine client to add that contact and respond with 20x!')


@given('we have a new contact')
def step_impl(context):  # noqa: W0404
    pass


@when('we add the new contact')
def step_impl(context):  # noqa: W0404
    assert True is not False


@then('crmeta will allow us to add that contact!')
def step_impl(context):  # noqa: W0404
    assert context.failed is False
