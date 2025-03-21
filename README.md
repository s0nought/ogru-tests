# ogru-tests

End-to-end tests for [old-games.ru](https://www.old-games.ru/)

Table of Contents:

- [Tests](#tests)
- [Stack](#stack)
- [Setup](#setup)
- [Scripts](#scripts)

## Tests

- **Authentication**
    - _Log in with username and password_

## Stack

- Pytest
- Playwright
- Allure

## Setup

Install prerequisites:

1. [Git](https://git-scm.com/downloads)
2. [Allure Report](https://allurereport.org/docs/install/)
3. [Python](https://www.python.org/downloads/)

Run in terminal:

```bash
$ git clone https://github.com/s0nought/ogru-tests.git
$ cd ogru-tests
$ cp .env.sample .env
$ python3 -m venv --clear --copies venv
$ source ./venv/bin/activate
$ pip3 install -r requirements.txt
$ playwright install
```

For activating venv in a different shell see [How venvs work](https://docs.python.org/3/library/venv.html#how-venvs-work).

Make sure to specify `OGRU_USER_LOGIN` and `OGRU_USER_PASSWORD` in `.env`.

## Scripts

|Name|Description|
|:---|:----------|
|`python3 main.py`|**Run end-to-end tests pipeline**|
