# Local Python Environment Setup

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

2. install browsers

```bash
    poetry run playwright install firefox
```

### Running code

poetry run python examples/math.py      

1. for scripts defined in the pyproject.toml

```bash
    poetry run hello-script
```

2. for python files

```bash
    poetry run python examples/math.py 
```

3. for running pytests

```bash
    poetry run pytest
```


### Playwright.
[playwright-python](https://playwright.dev/python/docs/intro),
Playwright recommends using the official Playwright Pytest plugin to write end-to-end tests.
It provides context isolation, running it on multiple browser configurations out of the box.


```bash
    poetry cache clear --all pypi     # Clear cache
    poetry env remove --all           # Reset environment
    rm poetry.lock && poetry install  # Start fresh

    # For parallel execution install
    poetry add --dev pytest-xdist 
    
    #  This tells pytest to run tests on 2 cores (you can increase this number based on how many CPU cores you want to utilize).
    --numprocesses 2 or -n 2
```

### Running playwright python in docker:
[running in docker](https://playwright.dev/python/docs/docker),
[docker-image](https://hub.docker.com/r/microsoft/playwright-python)


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