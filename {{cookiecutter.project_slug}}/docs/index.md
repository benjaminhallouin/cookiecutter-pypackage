# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions?query=workflow%3ACI)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

Welcome to the documentation for **{{ cookiecutter.project_name }}**!

## Features

- ✨ Modern Python package structure (src-layout)
- 🚀 Built with the latest Python standards (PEP 621, PEP 517)
- 🔒 Ultra-strict code quality (Ruff, MyPy, pre-commit)
- 🧪 Comprehensive testing with pytest
- 📚 Beautiful documentation with Material for MkDocs
- 🔄 Automated CI/CD with GitHub Actions
- 🔐 Security scanning (Bandit, Safety)
- 📦 Ready for PyPI distribution

## Quick Start

### Installation

Install from PyPI:

```bash
pip install {{ cookiecutter.project_slug }}
```

For development:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e ".[dev]"
```

### Usage

```python
import {{ cookiecutter.project_slug }}

# Your code here
```

{% if cookiecutter.include_cli == "yes" -%}
### Command-Line Interface

```bash
{{ cookiecutter.project_slug }} --help
```
{% endif -%}

## Development

### Setup Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install --install-hooks
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/test_version.py
```

### Code Quality

This project uses ultra-strict code quality tools:

- **Ruff**: Lightning-fast linting and formatting
- **MyPy**: Static type checking with strict mode
- **Bandit**: Security vulnerability scanning
- **Pre-commit**: Automated checks before each commit

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Run specific tools
ruff check .
mypy src/
bandit -r src/
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/LICENSE) file for details.

## Links

- **Documentation**: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/)
- **PyPI**: [https://pypi.org/project/{{ cookiecutter.project_slug }}/](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
- **Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
- **Issue Tracker**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
