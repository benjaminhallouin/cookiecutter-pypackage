# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- Core functionality

## [{{ cookiecutter.version }}] - {% now 'local', '%Y-%m-%d' %}

### Added
- Initial release of {{ cookiecutter.project_name }}
- Modern Python package structure with src-layout
- Comprehensive testing suite with pytest
- Type checking with MyPy (strict mode)
- Code quality tools: Ruff for linting and formatting
- Security scanning: Bandit, Safety, detect-secrets
- Pre-commit hooks for automated quality checks
- GitHub Actions CI/CD pipeline
- Multi-platform testing (Linux, macOS, Windows)
- Multi-version testing (Python 3.10, 3.11, 3.12, 3.13)
- Documentation with Material for MkDocs
- Automated PyPI publishing
- Code coverage reporting
{% if cookiecutter.include_cli == "yes" -%}
- Command-line interface with {% if cookiecutter.command_line_interface == "Click" %}Click{% elif cookiecutter.command_line_interface == "Typer" %}Typer{% endif %}
{% endif -%}

### Documentation
- Getting Started guide
- API reference with mkdocstrings
- Contributing guidelines
- Code of Conduct
- Comprehensive README

### Development
- Development environment setup
- Pre-commit hooks configuration
- Testing infrastructure
- Documentation build system

[Unreleased]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/compare/v{{ cookiecutter.version }}...HEAD
[{{ cookiecutter.version }}]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases/tag/v{{ cookiecutter.version }}
