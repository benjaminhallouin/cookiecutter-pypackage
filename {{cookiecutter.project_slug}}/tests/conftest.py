"""Configuration for pytest."""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def _reset_environment() -> None:
    """Reset environment variables between tests."""
