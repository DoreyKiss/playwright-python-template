# Template Repository for Playwright UI and API Testing

This repository serves as a template for setting up Playwright-based UI and API testing.  
It aims to provide a clean, reusable foundation for end-to-end and integration testing, including:

- Browser automation with Chromium, Firefox, and WebKit
- API mocking and testing support
- CI/CD integration (GitHub Actions) with [ctrf reporting](https://ctrf.io/)
- Containerized execution using Docker

### Local Python Environment Setup

this project uses [poetry](https://python-poetry.org/docs/#installing-with-pipx).

1. Install required tools, and select the environment.

```bash
    brew install poetry
    poetry env use python3.12 
```
2. check envs

```bash
    poetry env list 
    poetry env info  
```

3. If the virtual env is not active activate by hand.

```bash
    poetry env activate
```

4. install dependencies

```bash
    poetry install 
```

### Selecting the interpreter:

paste the output of this script to the interpreter path

```bash
    poetry env info --path 
```

### for a fresh start, try these:

```bash
    poetry cache clear --all pypi     # Clear cache
    poetry env remove --all           # Reset environment
    rm poetry.lock && poetry install  # Start fresh
```

### Adding packages using poetry:

1. adding dependencies

```bash
    poetry add requests
```

2. adding dev dependencies

```bash
    poetry add --dev pytest-playwright
```

4. install browsers

```bash
    poetry run playwright install firefox chromium
```

### Running code  

1. for running all pytests
```bash
    poetry run pytest
```

2. for playwright tests
```bash
    poetry run pytest -m playwright  
```

### Playwright.
[playwright-python](https://playwright.dev/python/docs/intro),
Playwright recommends using the official Playwright Pytest plugin to write end-to-end tests.
It provides context isolation, running it on multiple browser configurations out of the box.


```bash
    # For parallel execution install
    poetry add --dev pytest-xdist 
    
    #  This tells pytest to run tests on 2 cores (you can increase this number based on how many CPU cores you want to utilize).
    --numprocesses 2 or -n 2
```

### Extensions

[python](https://marketplace.visualstudio.com/items?itemName=ms-python.python),
[pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance),
[python debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy),
for  [toml](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) file,
for  [spell checking](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).

### Code Quality

[flake8](https://pypi.org/project/flake8/),
[isort](https://pypi.org/project/isort/),
[black](https://pypi.org/project/black/),


### Code Conventions

```bash
    Classes PascalCase class DogBowl:
    Files snake_case dog_bowl.py
    Functions camelCase def feedDog():
    Constants UPPER_SNAKE MAX_DOGS = 5
    Variables lower_snake dog_name = "Bodri"
```

### CI

[common test reporting format](https://github.com/infopulse/pytest-common-test-report-json),

1. validate your action via act
```bash
    brew install act  
    act pull_request --dryrun 
```