"""Tests for finger joint-limit validation."""

import pytest

from dexterous_hand.finger import Finger


@pytest.fixture
def finger() -> Finger:
    """Return a two-joint test finger."""
    return Finger(
        name="index",
        joint_names=["index_base", "index_tip"],
        lower_limits_rad=[0.0, 0.0],
        upper_limits_rad=[1.0, 1.2],
    )


def test_validate_positions_passes_within_limits(finger: Finger) -> None:
    finger.validate_positions([0.25, 0.8])


def test_validate_positions_raises_value_error_below_lower_limit(finger: Finger) -> None:
    with pytest.raises(ValueError, match="outside"):
        finger.validate_positions([-0.1, 0.8])


def test_validate_positions_raises_value_error_above_upper_limit(finger: Finger) -> None:
    with pytest.raises(ValueError, match="outside"):
        finger.validate_positions([0.25, 1.3])


def test_validate_positions_raises_value_error_for_wrong_joint_count(finger: Finger) -> None:
    with pytest.raises(ValueError, match="expected 2 joints"):
        finger.validate_positions([0.25])
