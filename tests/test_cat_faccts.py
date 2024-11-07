import requests
from pytest_bdd import scenarios, given, when, then

# Load feature file
scenarios('../features/cat_facts.feature')

# Define the Cat Facts API endpoint
CAT_FACTS_API = "https://catfact.ninja/fact"


@given("I have access to the Cat Facts API")
def access_cat_facts_api():
    pass  # Just a placeholder, no action needed here


@when("I request a random cat fact")
def request_random_cat_fact():
    response = requests.get(CAT_FACTS_API)
    return response


@then("I receive a valid response with a cat fact")
def valid_response_with_fact(request_random_cat_fact):
    response = request_random_cat_fact
    assert response.status_code == 200, "Expected status code 200"
    fact = response.json().get("fact")
    assert isinstance(fact, str) and fact, "Expected a non-empty fact about cats"


@then("the length of the fact should be between 10 and 200 characters")
def fact_length_within_range(request_random_cat_fact):
    response = request_random_cat_fact
    fact = response.json().get("fact")
    assert 10 <= len(fact) <= 200, "Expected fact length between 10 and 200 characters"
