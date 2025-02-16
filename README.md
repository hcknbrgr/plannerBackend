# 360 Planner
This project is for an AI based task organizer

## Setup
Backend "Three60Scheduler" : Django

Database: Currently using db.sqlite3

LLM: OpenAI

### Setting up the backend environment
* Create a virtual environment using python's baked in venv module:
    * `python -m venv .venv`
* Activate your venv
    * `./.venv/scripts/activate` if on a Windows environment
* Install dependencies using the `requirements.txt` file
    * `pip install -r requirements.txt`
* Install developer dependencies using the `requirements-dev.txt` file
    * `pip install -r requirements-dev.txt`
* Install pre-commit hooks
    * `pre-commit install`


### Updating Backend Dependencies
* Developer requirements will be manually added to `requirements-dev.txt` to minimize requirements for deployment.
* We use `pip-tools` to manage our `requirements.txt` field
    * Whenever we update any of our dependencies or add a new one, update the requirement in:
        * `pyproject.toml`
        * Run: `pip-compile --upgrade`
        * To update a specific package to the latest or a specific version use the `--upgrade-package` or -P flag:
            * example: `pip-compile --upgrade-package django`
            * navigate to the `requirements.txt` file and unindent all comments, fix-requirements tool will not allow it


### Starting the project -- Backend
* Open the folder containing the app:
* Confirm all migrations have been completed: `python manage.py makemigrations`
* Once migrations are made, migrate any changes: `python manage.py migrate`
* Run the backend server: `python manage.py runserver`

### Development Tools
* TDD -
    * Testing Suite: `pytest` and `pytest-django`
    * Fixtures replacement tool - `factory_boy`

# CHANGELOG
* 20250204 - Finished basic frontend implementation of API, included checkbox functionality for task completed
