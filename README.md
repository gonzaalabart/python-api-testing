# python-api-testing
API Testing demo with Pytest and Requests.
I used https://restful-booker.herokuapp.com/apidoc/index.html public API for tests

# Getting started
- To download and install pytest, run this command from the terminal: >pip install pytest
- To download and install requests, run this command from the terminal: >pip install requests

To ensure all dependencies are resolved in a CI environment, in one go, add them to a requirements.txt file.
Then run the following command : pip install -r requirements.txt

# Running Tests
- To run all tests: >python -m pytest
- To run only the smoke test suite >python -m pytest -m smoke
- To run only the regression test suite >python -m pytest -m regression

# Pendings
- The authorization is Basic, not Bearer so the method I created for it in authZ.py doesn't make sense
- Add more tests
- Parameterize URLs and Credentials based on the environment.
