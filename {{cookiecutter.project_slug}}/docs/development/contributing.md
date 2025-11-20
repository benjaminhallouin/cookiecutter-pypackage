# Contributing to {{ cookiecutter.project_name }}

Thank you for considering contributing to {{ cookiecutter.project_name }}! 🎉

## Code of Conduct

This project adheres to a [Code of Conduct](code-of-conduct.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, package version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- A clear and descriptive title
- Detailed description of the proposed feature
- Examples of how the feature would be used
- Why this enhancement would be useful

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the test suite
5. Commit your changes (`git commit -m 'feat: add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

### Prerequisites

- Python {{ cookiecutter.min_python_version }}+
- Git
- Pre-commit

### Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev,test,docs]"

# Install pre-commit hooks
pre-commit install --install-hooks
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test
pytest tests/test_version.py -v

# Run tests in parallel
pytest -n auto
```

### Code Quality

This project maintains **ultra-strict** code quality standards:

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Linting with Ruff
ruff check .
ruff check . --fix

# Formatting with Ruff
ruff format .

# Type checking with MyPy
mypy src/

# Security scanning
bandit -r src/
safety check
```

### Building Documentation

```bash
# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `perf:` - Performance improvements
- `test:` - Adding or updating tests
- `build:` - Build system changes
- `ci:` - CI/CD changes
- `chore:` - Other changes

Examples:

```bash
git commit -m "feat: add new validation method"
git commit -m "fix: resolve issue with configuration loading"
git commit -m "docs: update installation instructions"
```

## Code Style

### Python Style Guide

- Follow PEP 8 (enforced by Ruff)
- Use type hints for all functions
- Write docstrings in Google style
- Maximum line length: 100 characters

### Docstring Example

```python
def example_function(param1: str, param2: int) -> bool:
    """Short description of the function.

    Longer description if needed, explaining the function's purpose,
    behavior, and any important details.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of return value.

    Raises:
        ValueError: Description of when this error is raised.

    Examples:
        >>> example_function("test", 42)
        True
    """
    pass
```

## Testing Guidelines

- Write tests for all new features
- Maintain test coverage above 90%
- Use descriptive test names
- Follow the AAA pattern (Arrange, Act, Assert)

Example:

```python
def test_feature_does_something() -> None:
    """Test that feature does something correctly."""
    # Arrange
    input_data = "test"
    
    # Act
    result = some_function(input_data)
    
    # Assert
    assert result == "expected"
```

## Release Process

Releases are automated via GitHub Actions when a tag is pushed:

```bash
# Create and push a new tag
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin v0.2.0
```

Or use commitizen:

```bash
cz bump
git push --follow-tags
```

## Questions?

Feel free to open an issue or reach out to the maintainers at {{ cookiecutter.author_email }}.

Thank you for contributing! 🚀
