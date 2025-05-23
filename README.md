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

### Running playwright python in docker:

When we want our tests to be
[running in docker](https://playwright.dev/python/docs/docker), we have to use this image:
[docker-image](https://hub.docker.com/r/microsoft/playwright-python), or build our own.

1. assuming you already have docker installed use this command to pull and build the image
```bash
    make docker-setup
```

2. run the tests in a docker container but also the `--rm` flag in the docker run command tells Docker to: 🧹 Automatically remove the container after it exits
```bash
    make docker-run-pw-tests
```

3. look at the report using:
```bash
    make show-docker-report
```

4. For debugging purposes you might want to inspect the environment, run commands manually, or troubleshoot issues inside the container, you can start it in detached mode without automatically removing it with:
```bash
    make docker-pw-debug
```

5. For cleanup you might want to use:
```bash
    make docker-cleanup
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


### CI

[common test reporting format](https://github.com/infopulse/pytest-common-test-report-json),

1. validate your action via act
```bash
    brew install act  
    act pull_request --dryrun 
```