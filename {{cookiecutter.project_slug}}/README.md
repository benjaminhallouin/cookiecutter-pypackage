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

---

## ✨ Features

- 🚀 **Modern Python Package**: Built with latest standards (PEP 621, PEP 517, src-layout)
- 🔒 **Ultra-Strict Quality**: Ruff, MyPy (strict mode), Bandit, Safety checks
- 🧪 **Comprehensive Testing**: pytest with coverage, parallel execution, hypothesis
- 📚 **Beautiful Docs**: Material for MkDocs with automatic API documentation
- 🔄 **Full CI/CD**: Multi-platform testing, security scans, automated releases
- 🎯 **Type Safety**: 100% type hints with strict MyPy configuration
- 🛡️ **Security First**: Automated vulnerability scanning and secret detection
- 📦 **Distribution Ready**: Configured for PyPI publishing

## 📦 Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

### Development Installation

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e ".[dev,test,docs]"
pre-commit install
```

## 🚀 Quick Start

```python
import {{ cookiecutter.project_slug }}

# Check version
print({{ cookiecutter.project_slug }}.__version__)

# Your code here
```

{% if cookiecutter.include_cli == "yes" -%}
### Command-Line Interface

```bash
# Show help
{{ cookiecutter.project_slug }} --help

# Example usage
{{ cookiecutter.project_slug }} hello World
```
{% endif -%}

## 🛠️ Development

### Prerequisites

- Python {{ cookiecutter.min_python_version }}+
- Git
- Pre-commit

### Setup Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install --install-hooks

# Run tests
pytest

# Run all quality checks
pre-commit run --all-files
```

### Code Quality Standards

This project maintains **world-class** code quality standards:

#### Linting & Formatting
- **Ruff**: Ultra-fast linter and formatter (replaces flake8, isort, black)
- Enforces 600+ rules including:
  - PEP 8 compliance
  - Import sorting
  - Type annotations
  - Security best practices
  - Code complexity limits

#### Type Checking
- **MyPy**: Strict static type checking
- 100% type coverage required
- No `Any` types without justification
- Strict function signatures

#### Security
- **Bandit**: Security vulnerability scanner
- **Safety**: Dependency vulnerability checker
- **TruffleHog**: Secret detection
- **detect-secrets**: Pre-commit secret detection

#### Testing
- **pytest**: Test framework
- Minimum 90% code coverage
- Parallel test execution
- Property-based testing with Hypothesis

### Running Quality Checks

```bash
# Linting
ruff check .
ruff format .

# Type checking
mypy src/

# Security
bandit -r src/
safety check

# Tests with coverage
pytest --cov --cov-report=html

# All checks (runs in CI)
pre-commit run --all-files
```

### Documentation

```bash
# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) first.

### Contribution Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks
5. Commit with conventional commits (`feat:`, `fix:`, `docs:`, etc.)
6. Push to your fork
7. Open a Pull Request

### Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new validation feature
fix: resolve issue with configuration loading
docs: update installation instructions
test: add tests for edge cases
ci: update GitHub Actions workflow
```

## 📋 Project Structure

```
{{ cookiecutter.project_slug }}/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # Continuous Integration
│   │   └── release.yml          # Release automation
│   └── dependabot.yml           # Dependency updates
├── docs/                        # Documentation
│   ├── getting-started/
│   ├── development/
│   └── about/
├── src/
│   └── {{ cookiecutter.project_slug }}/
│       ├── __init__.py
│       ├── exceptions.py
│       ├── types.py
│       {% if cookiecutter.include_cli == "yes" -%}
│       └── cli.py
│       {% endif -%}
├── tests/                       # Test suite
│   ├── conftest.py
│   ├── test_version.py
│   └── test_exceptions.py
├── .pre-commit-config.yaml      # Pre-commit hooks
├── pyproject.toml               # Project configuration
├── mkdocs.yml                   # Documentation config
├── LICENSE
└── README.md
```

## 🔧 Configuration Files

- **pyproject.toml**: PEP 621 compliant project configuration
- **.pre-commit-config.yaml**: 15+ pre-commit hooks for code quality
- **mkdocs.yml**: Documentation configuration with Material theme
- **.github/workflows/**: Complete CI/CD pipeline

## 📊 GitHub Actions Workflows

### CI Pipeline
- ✅ Pre-commit checks
- ✅ Linting (Ruff)
- ✅ Type checking (MyPy)
- ✅ Security scanning (Bandit, Safety, TruffleHog)
- ✅ Tests on Python 3.10, 3.11, 3.12, 3.13
- ✅ Tests on Ubuntu, Windows, macOS
- ✅ Code coverage reporting
- ✅ Documentation build
- ✅ Package build verification

### Release Pipeline
- 📦 Automated PyPI publishing
- 📝 GitHub Release creation
- 📚 Documentation deployment
- 🏷️ Semantic versioning

## 📄 License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/)
- **PyPI**: [https://pypi.org/project/{{ cookiecutter.project_slug }}/](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
- **Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
- **Issue Tracker**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)

## 🙏 Acknowledgments

This project structure is inspired by best practices from the Python community and follows recommendations from:

- [PyPA](https://www.pypa.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

## 💬 Support

- 📫 Email: {{ cookiecutter.author_email }}
- 🐛 Issues: [GitHub Issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
- 💡 Discussions: [GitHub Discussions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/discussions)

---

Made with ❤️ by {{ cookiecutter.author_name }}
