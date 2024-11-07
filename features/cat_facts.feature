Feature: Cat Facts API Tests
  Test the functionality of the Cat Facts API

  Scenario: Retrieve a Random Cat Fact
    Given I have access to the Cat Facts API
    When I request a random cat fact
    Then I receive a valid response with a cat fact

  Scenario: Check Fact Length
    Given I have access to the Cat Facts API
    When I request a random cat fact
    Then the length of the fact should be between 10 and 200 characters
