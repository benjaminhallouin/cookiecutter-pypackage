# Contributing to {{ cookiecutter.project_name }}

First off, thank you for considering contributing to {{ cookiecutter.project_name }}! 🎉

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the [existing issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues) to avoid duplicates.

When you create a bug report, include as many details as possible:

- **Clear title**: Descriptive and specific
- **Description**: Detailed explanation of the issue
- **Steps to reproduce**: Step-by-step instructions
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment**:
  - OS and version
  - Python version
  - Package version
  - Relevant dependencies

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues).

Include:

- **Clear title**: Descriptive and specific
- **Detailed description**: Explain the enhancement
- **Use cases**: How would it be used?
- **Examples**: Code samples if applicable
- **Benefits**: Why would this be useful?

### Pull Requests

Pull requests are the best way to propose changes:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write or update tests
5. Update documentation
6. Ensure all tests pass
7. Submit a pull request

## Development Setup

### Prerequisites

- Python {{ cookiecutter.min_python_version }}+
- Git
- pip or uv

### Initial Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev,test,docs]"

# Install pre-commit hooks
pre-commit install --install-hooks
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Changes

Write your code following our [coding standards](#coding-standards).

### 3. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/test_your_feature.py

# Run in parallel
pytest -n auto
```

### 4. Check Code Quality

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Or run individual tools:
ruff check .                    # Linting
ruff format .                   # Formatting
mypy src/                       # Type checking
bandit -r src/                  # Security check
```

### 5. Update Documentation

If you've added or changed functionality:

```bash
# Serve docs locally
mkdocs serve

# Build docs
mkdocs build
```

### 6. Commit Changes

Follow our [commit message guidelines](#commit-messages):

```bash
git add .
git commit -m "feat: add your feature description"
```

### 7. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub.

## Coding Standards

### Python Style

- **PEP 8**: Follow Python style guide (enforced by Ruff)
- **Type hints**: All functions must have type hints
- **Docstrings**: Google-style docstrings for all public APIs
- **Line length**: Maximum 100 characters
- **Imports**: Organized by Ruff (stdlib, third-party, local)

### Type Hints

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

def process_items(items: Sequence[str], count: int = 10) -> list[str]:
    """Process a sequence of items.
    
    Args:
        items: The items to process.
        count: Maximum number of items to process.
    
    Returns:
        Processed items.
    """
    return list(items[:count])
```

### Docstrings

Use Google-style docstrings:

```python
def complex_function(
    param1: str,
    param2: int,
    param3: bool = False,
) -> dict[str, Any]:
    """Short one-line summary.

    Longer description of what the function does. Can span
    multiple lines and include details about implementation.

    Args:
        param1: Description of param1. Can span multiple
            lines if needed.
        param2: Description of param2.
        param3: Description of param3. Defaults to False.

    Returns:
        Description of return value. Can include type
        information and structure details.

    Raises:
        ValueError: If param2 is negative.
        TypeError: If param1 is not a string.

    Examples:
        >>> complex_function("test", 42)
        {'result': 'test', 'count': 42}
        
        >>> complex_function("test", -1)
        Traceback (most recent call last):
            ...
        ValueError: param2 must be positive
    """
    if param2 < 0:
        raise ValueError("param2 must be positive")
    
    return {"result": param1, "count": param2}
```

### Code Organization

```python
"""Module docstring."""

from __future__ import annotations

# Standard library imports
import os
import sys
from pathlib import Path

# Third-party imports
import requests
from rich.console import Console

# Local imports
from {{ cookiecutter.project_slug }}.exceptions import CustomError
from {{ cookiecutter.project_slug }}.types import CustomType

# Type checking imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator

# Module-level constants
DEFAULT_VALUE = 42

# Code here
```

## Testing Guidelines

### Writing Tests

- **Test coverage**: Aim for >90% coverage
- **Test naming**: Use descriptive names (`test_function_does_something`)
- **AAA pattern**: Arrange, Act, Assert
- **Fixtures**: Use pytest fixtures for setup
- **Markers**: Use markers for slow/integration tests

### Test Example

```python
"""Tests for feature X."""

from __future__ import annotations

import pytest

from {{ cookiecutter.project_slug }}.module import function_to_test


def test_function_with_valid_input() -> None:
    """Test function with valid input."""
    # Arrange
    input_value = "test"
    expected = "TEST"
    
    # Act
    result = function_to_test(input_value)
    
    # Assert
    assert result == expected


def test_function_raises_error_with_invalid_input() -> None:
    """Test function raises error with invalid input."""
    with pytest.raises(ValueError, match="Invalid input"):
        function_to_test("")


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        ("hello", "HELLO"),
        ("world", "WORLD"),
        ("123", "123"),
    ],
)
def test_function_with_multiple_inputs(
    input_value: str,
    expected: str,
) -> None:
    """Test function with multiple inputs."""
    assert function_to_test(input_value) == expected


@pytest.mark.slow
def test_slow_operation() -> None:
    """Test that takes a long time."""
    # Mark as slow so it can be skipped with -m "not slow"
    pass
```

### Running Specific Tests

```bash
# Run specific test file
pytest tests/test_feature.py

# Run specific test
pytest tests/test_feature.py::test_specific_function

# Run tests matching pattern
pytest -k "test_feature"

# Skip slow tests
pytest -m "not slow"

# Run with coverage
pytest --cov=src/{{ cookiecutter.project_slug }} --cov-report=html
```

## Documentation

### Building Documentation

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Serve locally (with live reload)
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

### Writing Documentation

- **Markdown**: All docs in Markdown format
- **Structure**: Follow existing structure in `docs/`
- **Code examples**: Include working examples
- **Links**: Use relative links for internal references

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Build system changes
- `ci`: CI/CD changes
- `chore`: Other changes (dependencies, etc.)

### Examples

```bash
# Simple commit
git commit -m "feat: add user authentication"

# With scope
git commit -m "fix(api): handle timeout errors"

# With body
git commit -m "feat: add caching layer

Implement Redis-based caching for API responses.
Reduces database load by 50%."

# Breaking change
git commit -m "feat!: redesign configuration API

BREAKING CHANGE: Configuration now uses TOML instead of JSON.
Users must migrate their config files."
```

### Using Commitizen

```bash
# Interactive commit
cz commit

# Create bump version
cz bump
```

## Pull Request Process

### Before Submitting

1. ✅ Update documentation
2. ✅ Add tests for new features
3. ✅ Run full test suite
4. ✅ Run pre-commit hooks
5. ✅ Update CHANGELOG.md
6. ✅ Ensure CI passes

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Coverage maintained/improved

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Tests added/updated
- [ ] CHANGELOG updated
```

### Review Process

1. **Automated checks**: CI must pass
2. **Code review**: Maintainer review required
3. **Testing**: Verify tests cover changes
4. **Documentation**: Check docs are updated
5. **Merge**: Squash and merge when approved

## Questions?

- 📧 Email: {{ cookiecutter.author_email }}
- 💬 Discussions: [GitHub Discussions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)

Thank you for contributing! 🚀
