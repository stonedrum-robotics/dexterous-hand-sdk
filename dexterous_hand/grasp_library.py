"""Predefined grasp poses and lookup helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GraspPose:
    """A named joint target suitable for repeatable demonstrations."""

    name: str
    joint_positions_rad: dict[str, float]
    description: str


class GraspLibrary:
    """Small library of common grasp primitives."""

    def __init__(self, poses: dict[str, GraspPose] | None = None) -> None:
        self._poses = poses or self.default_poses()

    @staticmethod
    def default_poses() -> dict[str, GraspPose]:
        """Return conservative mock poses for initial demos."""
        return {
            "open": GraspPose("open", {}, "Open relaxed posture."),
            "pinch": GraspPose(
                "pinch",
                {
                    "thumb_flex": 0.65,
                    "index_flex": 0.7,
                    "middle_flex": 0.15,
                },
                "Thumb-index pinch for small objects.",
            ),
            "cylindrical": GraspPose(
                "cylindrical",
                {
                    "thumb_flex": 0.55,
                    "index_flex": 0.9,
                    "middle_flex": 0.9,
                    "ring_flex": 0.9,
                    "little_flex": 0.9,
                },
                "Power grasp for cylindrical objects.",
            ),
        }

    def get(self, name: str) -> GraspPose:
        """Return a named grasp pose."""
        try:
            return self._poses[name]
        except KeyError as exc:
            raise KeyError(f"Unknown grasp pose: {name}") from exc

    def names(self) -> list[str]:
        """List available grasp names."""
        return sorted(self._poses)
