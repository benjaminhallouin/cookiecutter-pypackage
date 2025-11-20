"""Tests for {{ cookiecutter.project_slug }}."""

from __future__ import annotations

import {{ cookiecutter.project_slug }}


def test_version() -> None:
    """Test version is defined."""
    assert {{ cookiecutter.project_slug }}.__version__
    assert isinstance({{ cookiecutter.project_slug }}.__version__, str)
    assert len({{ cookiecutter.project_slug }}.__version__.split(".")) >= 3


def test_author() -> None:
    """Test author is defined."""
    assert {{ cookiecutter.project_slug }}.__author__
    assert isinstance({{ cookiecutter.project_slug }}.__author__, str)


def test_email() -> None:
    """Test email is defined."""
    assert {{ cookiecutter.project_slug }}.__email__
    assert isinstance({{ cookiecutter.project_slug }}.__email__, str)
    assert "@" in {{ cookiecutter.project_slug }}.__email__
