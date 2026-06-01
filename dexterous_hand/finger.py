"""Finger and joint domain models."""

from dataclasses import dataclass


@dataclass(frozen=True)
class JointState:
    """State for a single actuated joint."""

    name: str
    position_rad: float
    velocity_rad_s: float = 0.0
    effort_nm: float = 0.0


@dataclass
class Finger:
    """A named finger with ordered joints and safety limits."""

    name: str
    joint_names: list[str]
    lower_limits_rad: list[float]
    upper_limits_rad: list[float]

    def validate_positions(self, positions_rad: list[float]) -> None:
        """Validate joint positions against configured limits."""
        if len(positions_rad) != len(self.joint_names):
            msg = f"{self.name} expected {len(self.joint_names)} joints, got {len(positions_rad)}"
            raise ValueError(msg)

        for joint, value, lower, upper in zip(
            self.joint_names, positions_rad, self.lower_limits_rad, self.upper_limits_rad
        ):
            if value < lower or value > upper:
                msg = f"{joint} position {value:.3f} rad outside [{lower:.3f}, {upper:.3f}]"
                raise ValueError(msg)
