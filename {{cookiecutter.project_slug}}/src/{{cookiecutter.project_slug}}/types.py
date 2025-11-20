"""Type hints and type aliases for {{ cookiecutter.project_slug }}."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any, TypeVar

    T = TypeVar("T")

__all__: list[str] = []
