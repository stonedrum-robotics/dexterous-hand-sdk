"""Pytest configuration for the SDK."""

import pytest

from dexterous_hand import Hand


@pytest.fixture
def mock_hand() -> Hand:
    """Return a connected mock hand."""
    return Hand.mock()
