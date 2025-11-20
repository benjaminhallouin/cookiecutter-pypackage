# Cookiecutter Python Package Template 🚀

A world-class, production-ready Python package template with ultra-strict code quality standards and comprehensive CI/CD.

## 🎯 Features

### 📦 Modern Package Structure
- **src-layout**: Industry best practice
- **PEP 621**: Modern pyproject.toml configuration
- **PEP 517**: Modern build system (Hatchling)
- **Type hints**: Full type coverage with py.typed marker

### 🔒 Ultra-Strict Code Quality
- **Ruff**: Lightning-fast linting & formatting (600+ rules)
- **MyPy**: Strict type checking (no Any types)
- **Bandit**: Security vulnerability scanning
- **Safety**: Dependency vulnerability checking
- **Pre-commit**: 15+ hooks for automated quality checks

### 🧪 Comprehensive Testing
- **pytest**: Modern testing framework
- **Coverage**: 90%+ requirement with branch coverage
- **Parallel execution**: Fast test runs with pytest-xdist
- **Property-based testing**: Hypothesis integration
- **Multi-platform**: Linux, macOS, Windows
- **Multi-version**: Python 3.10, 3.11, 3.12, 3.13

### 📚 Beautiful Documentation
- **Material for MkDocs**: Modern, responsive design
- **Automatic API docs**: mkdocstrings integration
- **Code examples**: Syntax highlighting
- **Search**: Built-in search functionality
- **Dark mode**: Automatic theme switching

### 🔄 Complete CI/CD
- **GitHub Actions**: Full automation
- **Multi-stage pipeline**: Lint, test, build, deploy
- **Security scanning**: Bandit, Safety, TruffleHog
- **Automated releases**: PyPI + GitHub Releases
- **Documentation deployment**: GitHub Pages
- **Dependency updates**: Dependabot/Renovate

## 🚀 Quick Start

### Prerequisites

```bash
pip install cookiecutter
```

### Create a New Package

```bash
# From GitHub (recommended)
cookiecutter gh:benjaminhallouin/cookiecutter-pypackage

# Or from local directory
cookiecutter .
```

### Configuration Options

You'll be prompted for:

- **project_name**: Your project name (e.g., "My Python Package")
- **project_slug**: Package name (auto-generated)
- **project_short_description**: Brief description
- **author_name**: Your name
- **author_email**: Your email
- **github_username**: Your GitHub username
- **version**: Initial version (default: 0.1.0)
- **python_version**: Target Python version (default: 3.12)
- **min_python_version**: Minimum Python version (default: 3.10)
- **license**: MIT, Apache-2.0, BSD-3-Clause, GPL-3.0, Proprietary
- **use_docker**: Include Dockerfile (yes/no)
- **use_github_actions**: Include GitHub Actions (yes/no)
- **use_precommit**: Include pre-commit (yes/no)
- **use_mkdocs**: Include MkDocs (yes/no)
- **use_dependabot**: Use Dependabot (yes/no)
- **use_renovate**: Use Renovate (no/yes)
- **command_line_interface**: Click, Typer, Argparse, None
- **include_cli**: Include CLI (yes/no)

## 📋 Generated Project Structure

```
your-package/
├── .github/workflows/        # CI/CD pipelines
├── docs/                     # Documentation
├── src/your_package/         # Source code (src-layout)
├── tests/                    # Test suite
├── .pre-commit-config.yaml   # 15+ pre-commit hooks
├── pyproject.toml            # PEP 621 configuration
├── mkdocs.yml               # Documentation config
└── README.md                # Project README
```

## 🔧 After Generation

### 1. Initialize Git & Install

```bash
cd your-package
git init
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,test,docs]"
pre-commit install --install-hooks
```

### 2. Run Tests & Checks

```bash
pytest                        # Run tests
pre-commit run --all-files   # Run all checks
mkdocs serve                 # Serve documentation
```

### 3. Push to GitHub

```bash
git add .
git commit -m "chore: initial commit"
git remote add origin https://github.com/username/your-package.git
git push -u origin main
```

### 4. Configure Secrets

Add to GitHub repository secrets:
- `CODECOV_TOKEN`: For coverage reporting
- `PYPI_API_TOKEN`: For PyPI publishing

## 🎨 What Makes This World-Class?

### Code Quality
- **600+ Ruff rules** - All best practices enforced
- **Strict MyPy** - 100% type coverage
- **15+ pre-commit hooks** - Automated quality gates
- **Security scanning** - Bandit, Safety, TruffleHog, detect-secrets

### Testing
- **90%+ coverage** requirement
- **Multi-platform** testing (Linux, macOS, Windows)
- **Multi-version** testing (Python 3.10-3.13)
- **Parallel execution** with pytest-xdist
- **Property-based testing** with Hypothesis

### CI/CD Pipeline

**CI Workflow:**
1. ✅ Pre-commit checks
2. ✅ Linting (Ruff)
3. ✅ Type checking (MyPy)
4. ✅ Security scanning
5. ✅ Multi-platform/version tests
6. ✅ Coverage reporting
7. ✅ Documentation build
8. ✅ Package verification

**Release Workflow:**
1. 📦 Build package
2. 🚀 Publish to PyPI
3. 📝 Create GitHub Release
4. 📚 Deploy documentation

## 📄 License

MIT License - Projects generated can use any license.

## 🙏 Acknowledgments

Inspired by [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) and Python community best practices.

---

**Made with ❤️ for the Python community**