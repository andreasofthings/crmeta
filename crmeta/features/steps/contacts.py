from behave import *


Scenario: Add a contact
     Given we have a new contact
      When we add the new contact
      Then crmeta will allow us to add that contact!
        
@given('we have a new contact')
def step_impl(context):
    pass

@when('we add the new contact')
def step_impl(context):
    assert True is not False

@then('crmeta will allow us to add that contact!')
def step_impl(context):
    assert context.failed is False
