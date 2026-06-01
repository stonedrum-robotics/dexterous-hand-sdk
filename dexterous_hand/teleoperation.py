"""Teleoperation interfaces."""

from __future__ import annotations

from dataclasses import dataclass

from dexterous_hand.hand import Hand


@dataclass(frozen=True)
class TeleoperationFrame:
    """Normalized teleoperation command frame."""

    joint_targets_rad: dict[str, float]
    source: str = "unknown"


class TeleoperationController:
    """Maps teleoperation frames to hand commands."""

    def __init__(self, hand: Hand) -> None:
        self.hand = hand

    def apply_frame(self, frame: TeleoperationFrame) -> None:
        """Apply a normalized teleoperation command."""
        if not frame.joint_targets_rad:
            return
        self.hand.move_joints(frame.joint_targets_rad)

    def read_glove_frame(self) -> TeleoperationFrame:
        """Read a glove frame from a configured device."""
        raise NotImplementedError("Glove device integration is vendor-specific.")
