# Stellar Burgers UI Tests

UI test automation project for the Stellar Burgers web application: a burger-constructor web app with user accounts.

The project demonstrates automated browser testing with Python, pytest, and Selenium WebDriver: user-flow coverage, form validation checks, reusable fixtures, generated test data, and protection against an unavailable external test environment.

## Tech stack

* Python
* pytest
* Selenium WebDriver (Chrome)
* Faker

## Test suite at a glance

17 tests, grouped by user flow:

| File | Tests | What is covered |
|---|---|---|
| `test_registration.py` | 6 | opening the registration form; successful registration; validation of an empty name, an invalid email, and a short password, including the error text |
| `test_logging_in.py` | 4 | login from four entry points: the main page button, the "Personal account" link, the registration form, and the password-recovery form |
| `test_constructor_section.py` | 3 | switching between the constructor sections: buns, sauces, and fillings |
| `test_account_to_constructor_switching.py` | 2 | navigation from the personal account to the constructor via the "Constructor" link and the logo |
| `test_entering_account_page.py` | 1 | opening the personal account as a logged-in user |
| `test_logging_out.py` | 1 | logout from the personal account |

## Project structure

* `tests/` - UI test cases
* `add/` - configuration, locators, helpers, and test data
* `conftest.py` - pytest fixtures: browser setup, environment check, test-account credentials
* `requirements.txt` - project dependencies
* `.env.example` - environment variables and their default values

## Requirements

* Python 3.10+
* Google Chrome. Selenium Manager downloads a matching ChromeDriver automatically.

## How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run tests with detailed output and short tracebacks:

```bash
pytest -v --tb=short
```

Tests open a visible Chrome window.

## Environment

| Variable | Default | Purpose |
|---|---|---|
| `BASE_URL` | `https://stellarburgers.nomoreparties.site` | Application under test |
| `TEST_EMAIL` | none | Test account for login-dependent tests |
| `TEST_PASSWORD` | none | Password of the test account |

Example:

```bash
BASE_URL=https://example.com TEST_EMAIL=your_test_account@example.com TEST_PASSWORD=your_test_password pytest
```

Login-dependent tests are skipped with a clear reason if `TEST_EMAIL` and `TEST_PASSWORD` are not set. Credentials are never stored in the repository.

## External environment availability

The suite runs against a public demo environment that this project does not control.

If the base URL is unavailable, the tests are skipped with a clear reason instead of failing during browser setup:

```text
SKIPPED: Base URL is not available
```

## Notes

This repository is a portfolio version of a UI test automation project.
