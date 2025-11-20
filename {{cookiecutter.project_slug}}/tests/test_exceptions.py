"""Tests for {{ cookiecutter.project_slug }} exceptions."""

from __future__ import annotations

import pytest

from {{ cookiecutter.project_slug }}.exceptions import (
    ConfigurationError,
    ValidationError,
    {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error,
)


def test_base_exception() -> None:
    """Test base exception."""
    with pytest.raises({{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error):
        raise {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error("test error")


def test_configuration_error() -> None:
    """Test configuration error."""
    with pytest.raises(ConfigurationError):
        raise ConfigurationError("config error")


def test_validation_error() -> None:
    """Test validation error."""
    with pytest.raises(ValidationError):
        raise ValidationError("validation error")


def test_exception_inheritance() -> None:
    """Test exception inheritance."""
    assert issubclass(ConfigurationError, {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error)
    assert issubclass(ValidationError, {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error)
