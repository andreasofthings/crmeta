@crm @contacts 
Feature: Contact Management
  Contact Management provides functionality to manage contact details.
  The feature is accessible through Django Admin in first place, but also a Django Rest Framework API.

  Background: the contact database is already filled with some contacts
    Given a client works with the component

  Scenario: Add a contact
     Given a machine client has a new contact
      When a machine client adds the new contact
      Then crmeta will allow the machine client to add that contact and respond with 20x!
      
  Scenario: Update a contact
     Given a machine client has a new detail for an existing contact
      When a machine client adds the detail
      Then crmeta will allow the machine client to change that contact and respond with 20x!
