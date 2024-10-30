# Assistant API - Backend

## Requirements

* [Docker](https://www.docker.com/).
* [uv](https://docs.astral.sh/uv/) for Python package and environment management.

## General Workflow

### Dependencies management

By default, the dependencies are managed with [uv](https://docs.astral.sh/uv/), go there and install it.

You can install all the dependencies with:

```console
$ uv sync
```

Then you can activate the virtual environment with:

```console
$ source .venv/bin/activate
```

Make sure your editor is using the correct Python virtual environment, with the interpreter at `.venv/bin/python`.

### Used tools

- `pytest`, `coverage` - testing
- `mypy`, `ruff` - lints and static code analysis
- `pre-commit` - pre-commit hooks

# Source information

Project is based on https://github.com/fastapi/full-stack-fastapi-template/tree/master. Go there for more examples