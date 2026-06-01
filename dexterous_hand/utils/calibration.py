"""Calibration helpers."""


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
