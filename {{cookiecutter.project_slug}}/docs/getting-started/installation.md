# Installation

## From PyPI

The simplest way to install {{ cookiecutter.project_name }} is from PyPI:

```bash
pip install {{ cookiecutter.project_slug }}
```

## From Source

To install the latest development version from source:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e .
```

## Development Installation

For development work, install with all dependencies:

```bash
pip install -e ".[dev,test,docs]"
```

### Prerequisites

- Python {{ cookiecutter.min_python_version }}+
- pip 23.0+

## Virtual Environment

It's recommended to use a virtual environment:

=== "venv"

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install {{ cookiecutter.project_slug }}
    ```

=== "conda"

    ```bash
    conda create -n {{ cookiecutter.project_slug }} python={{ cookiecutter.python_version }}
    conda activate {{ cookiecutter.project_slug }}
    pip install {{ cookiecutter.project_slug }}
    ```

=== "uv"

    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    uv pip install {{ cookiecutter.project_slug }}
    ```
