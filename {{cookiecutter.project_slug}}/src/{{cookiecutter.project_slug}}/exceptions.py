"""Exceptions for {{ cookiecutter.project_slug }}."""

from __future__ import annotations


class {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error(Exception):
    """Base exception for {{ cookiecutter.project_slug }}."""


class ConfigurationError({{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error):
    """Raised when there is a configuration error."""


class ValidationError({{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}Error):
    """Raised when validation fails."""
