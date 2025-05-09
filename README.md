# Local Python Environment Setup

this project uses [poetry](https://python-poetry.org/docs/#installing-with-pipx).

1. Install required tools

```bash
    brew install poetry
    brew install direnv 
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

### Code Conventions

```bash
    Classes PascalCase class DogBowl:
    Files snake_case dog_bowl.py
    Functions camelCase def feedDog():
    Constants UPPER_SNAKE MAX_DOGS = 5
    Variables lower_snake dog_name = "Bodri"
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

poetry run pytest

### Extensions

[python](https://marketplace.visualstudio.com/items?itemName=ms-python.python),
[pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance),
[python debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy),
for  [toml](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) file,
for  [spell checking](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).

### Code Quality

[flake8](https://pypi.org/project/flake8/),
[isort](https://pypi.org/project/isort/),
[safety](https://pypi.org/project/safety/),

