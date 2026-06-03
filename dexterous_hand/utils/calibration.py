"""Calibration helpers."""

from __future__ import annotations

from dexterous_hand.hand import Hand


def normalize_raw_joint(raw_value: float, raw_min: float, raw_max: float) -> float:
    """Normalize a raw sensor value to [0, 1]."""
    if raw_max <= raw_min:
        raise ValueError("raw_max must be greater than raw_min")
    return max(0.0, min(1.0, (raw_value - raw_min) / (raw_max - raw_min)))


def interpolate_joint(normalized: float, lower_rad: float, upper_rad: float) -> float:
    """Map a normalized joint value into a physical range."""
    if not 0.0 <= normalized <= 1.0:
        raise ValueError("normalized must be in [0, 1]")
    return lower_rad + normalized * (upper_rad - lower_rad)


def calibrate_hand(hand: Hand) -> dict[str, float]:
    """Calibrate a hand by homing every known joint to its zero position.

    The routine reads the connected hand, commands each currently visible joint
    to `0.0` radians, reads the resulting position, and records that measured
    value as the software offset. For the mock driver the offsets will normally
    be zero. On physical Linkerbot hardware, `[VENDOR_SDK_REQUIRED]`: the same
    sequence must be paired with the vendor SDK's persistent offset write,
    encoder-zero command, or non-volatile calibration storage before the values
    are trusted for production use.

    Args:
        hand: Connected hand instance to calibrate.

    Returns:
        Mapping from joint name to measured zero-offset position in radians.

    Raises:
        RuntimeError: Propagated from the driver if the hand is not connected.
        KeyError: Propagated if the driver rejects a joint command.
    """
    initial_states = hand.read_joints()
    offsets: dict[str, float] = {}

    for state in initial_states:
        joint_name = state.name
        hand.move_joints({joint_name: 0.0})

        measured = {joint.name: joint.position_rad for joint in hand.read_joints()}
        offsets[joint_name] = measured[joint_name]

    return offsets
