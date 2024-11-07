# Cat Facts API Test Cases

## Project Description
This project contains automated test cases for the Cat Facts API using `pytest-bdd`, a behavior-driven testing framework. The purpose of these tests is to verify that the API provides valid, meaningful facts about cats and meets quality criteria such as appropriate response status and fact length.

## Setup Instructions

### 1. Clone the Repository
To get started, first clone the repository to your local machine. This step downloads the project files to your computer.

```bash
git clone https://github.com/your-username/Cat-Facts-API-Tests.git
cd Cat-Facts-API-Tests
```

### 2. Create a Virtual Environment (Recommended)
Setting up a virtual environment helps to manage dependencies specifically for this project, avoiding conflicts with other projects on your machine.

Run this command to create a virtual environment named env:

```bash
python -m venv env
```

### 3. Activate the Virtual Environment
Before installing dependencies, activate the virtual environment.

On Windows:
```
.\env\Scripts\activate
```
On Mac:
```bash
source env/bin/activate

```
### 4. Install Dependencies
The required packages are listed in requirements.txt. This file specifies all dependencies needed to run the tests, including:

requests for making HTTP requests,
pytest for testing,
pytest-bdd for behavior-driven development.
Install these packages with the following command:
```bash

pip install -r requirements.txt
```
### 5. Run Tests
To execute the tests, use the following command in your terminal. This will run all test scenarios defined for the Cat Facts API.

```bash
pytest
```
If the tests pass, you’ll see output indicating successful execution. If any tests fail, pytest will display an error message with details.

Test Cases
The project includes two primary test cases for the Cat Facts API. These tests are written using pytest-bdd and are defined in both feature files and Python test files.

### Test Case	Steps	Expected Result	Validation
## Explanation of Each Test

    Retrieve a Random Cat Fact
    Purpose: To verify that the Cat Facts API returns a random fact with a successful response.
    Steps:
    Access the Cat Facts API.
    Send a request to retrieve a random cat fact.
    Expected Result:
    The API should return a 200 OK status code.
    The response should contain a fact field with a non-empty string.
    Validation:
    The test checks the response status code to ensure the request was successful.
    It then verifies that the fact field contains text, confirming that a valid cat fact was returned.
    Check Fact Length

    Purpose: To ensure that the length of the retrieved cat fact is within a reasonable range.
    Steps:
    Access the Cat Facts API.
    Send a request to retrieve a random cat fact.
    Expected Result:
    The response should have a 200 OK status code.
    The length of the fact should be between 10 and 200 characters.
    Validation:
    The test checks the response status code.
    It then checks the length of the fact field, confirming that the fact length is within an acceptable range for readability.
