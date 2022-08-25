from behave import given, when, then


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):  # noqa: W0404
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):  # noqa: W0404
    print(f"context: {context}")
    print(f"context.failed: {context.failed}")
    assert context.failed is False
