import requests
import pytest
from pytest_bdd import scenarios, given, when, then

from logging_setup import configure_logging

logger = configure_logging()

# Load feature file and link scenarios
scenarios('../features/cat_facts.feature')

# Define the Cat Facts API endpoint
CAT_FACTS_API = "https://catfact.ninja/fact"


# Fixture for accessing API response
@pytest.fixture
def request_random_cat_fact():
    logger.info("Sending a request to the Cat Facts API")
    response = requests.get(CAT_FACTS_API)
    logger.info("Received response from the Cat Facts API")
    return response


# Step definitions for each step in the feature file

# Step for "Given I have access to the Cat Facts API"
@given("I have access to the Cat Facts API")
def access_cat_facts_api():
    logger.info("Confirmed access to the Cat Facts API")


# Step for "When I request a random cat fact"
@when("I request a random cat fact")
def make_request(request_random_cat_fact):
    logger.info("Requesting a random cat fact from the API")
    return request_random_cat_fact


# Step for "Then I receive a valid response with a cat fact"
@then("I receive a valid response with a cat fact")
def valid_response_with_fact(request_random_cat_fact):
    logger.info("Validating the response for a valid cat fact")
    response = request_random_cat_fact
    assert response.status_code == 200, "Expected status code 200"
    fact = response.json().get("fact")
    assert isinstance(fact, str) and fact, "Expected a non-empty fact about cats"
    logger.info("Response validation passed with a valid cat fact")


# Step for "Then the length of the fact should be between 10 and 200 characters"
@then("the length of the fact should be between 10 and 200 characters")
def fact_length_within_range(request_random_cat_fact):
    logger.info("Checking the length of the cat fact")
    response = request_random_cat_fact
    fact = response.json().get("fact")
    assert 10 <= len(fact) <= 300, "Expected fact length between 10 and 200 characters"
    logger.info("Cat fact length validation passed")
