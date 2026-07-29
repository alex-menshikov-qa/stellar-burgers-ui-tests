# Stellar Burgers UI Tests

UI test automation project for the Stellar Burgers web application.

The project demonstrates automated browser testing using Python, Pytest, Selenium WebDriver, and Chrome WebDriver.

## Tech stack

* Python
* Pytest
* Selenium WebDriver
* Chrome WebDriver
* Faker

## Test coverage

The test suite covers the main user-facing flows of the application:

* user registration
* login from different entry points
* logout
* navigation to the personal account
* navigation from the personal account to the constructor
* switching between constructor sections:
  * buns
  * sauces
  * fillings
* registration form validation

## Project structure

* `tests/` - UI test cases
* `add/` - project configuration, locators, helpers, and test data
* `conftest.py` - Pytest fixtures and browser setup
* `requirements.txt` - project dependencies
* `.env.example` - default environment configuration

## How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Run tests with short traceback output:

```bash
pytest -v --tb=short
```

## Environment

By default, the tests run against the public demo site:

```text
https://stellarburgers.nomoreparties.site
```

The base URL can be overridden with an environment variable:

```bash
BASE_URL=https://example.com pytest
```

Default values are listed in `.env.example`.

## External environment availability

The test suite depends on an external public demo environment.

If the base URL is unavailable, the tests are skipped with a clear reason instead of failing during browser setup.

Example:

```text
SKIPPED: Base URL is not available
```

## Notes

This repository is a portfolio version of a UI test automation project.

It demonstrates UI test design, Selenium WebDriver usage, Pytest fixtures, generated test data, and basic protection against unavailable external test environments.