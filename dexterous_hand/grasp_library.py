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
    """Library of common grasp primitives for demos and tests."""

    def __init__(self, poses: dict[str, GraspPose] | None = None) -> None:
        self._poses = poses or self.default_poses()

    @staticmethod
    def default_poses() -> dict[str, GraspPose]:
        """Return conservative Cutkosky-inspired mock poses for initial demos."""
        return {
            "relaxed_open": GraspPose(
                "relaxed_open",
                {
                    "thumb_flex": 0.08,
                    "index_flex": 0.08,
                    "middle_flex": 0.08,
                    "ring_flex": 0.08,
                    "little_flex": 0.08,
                },
                "Slightly open rest posture for transport, inspection, and safe idle demos.",
            ),
            "precision_pinch": GraspPose(
                "precision_pinch",
                {
                    "thumb_flex": 0.65,
                    "index_flex": 0.7,
                    "middle_flex": 0.12,
                    "ring_flex": 0.08,
                    "little_flex": 0.08,
                },
                "Thumb and index fingertip contact for small objects such as pegs or beads.",
            ),
            "tripod": GraspPose(
                "tripod",
                {
                    "thumb_flex": 0.7,
                    "index_flex": 0.65,
                    "middle_flex": 0.62,
                    "ring_flex": 0.18,
                    "little_flex": 0.18,
                },
                "Three-point precision grasp for pens, markers, and small tools.",
            ),
            "lateral_pinch": GraspPose(
                "lateral_pinch",
                {
                    "thumb_flex": 0.72,
                    "index_flex": 0.38,
                    "middle_flex": 0.22,
                    "ring_flex": 0.18,
                    "little_flex": 0.18,
                },
                "Thumb pad against the side of the index finger for cards, keys, or tags.",
            ),
            "index_point": GraspPose(
                "index_point",
                {
                    "thumb_flex": 0.42,
                    "index_flex": 0.0,
                    "middle_flex": 0.82,
                    "ring_flex": 0.84,
                    "little_flex": 0.86,
                },
                "Index finger extended with other digits curled for buttons or touch targets.",
            ),
            "cylindrical_power": GraspPose(
                "cylindrical_power",
                {
                    "thumb_flex": 0.55,
                    "index_flex": 0.9,
                    "middle_flex": 0.9,
                    "ring_flex": 0.9,
                    "little_flex": 0.9,
                },
                "Power grasp wrapping all fingers around a cylindrical object or handle.",
            ),
            "spherical_power": GraspPose(
                "spherical_power",
                {
                    "thumb_flex": 0.62,
                    "index_flex": 0.78,
                    "middle_flex": 0.82,
                    "ring_flex": 0.78,
                    "little_flex": 0.72,
                },
                "Spread-finger power grasp for balls, knobs, and rounded objects.",
            ),
            "hook": GraspPose(
                "hook",
                {
                    "thumb_flex": 0.05,
                    "index_flex": 1.05,
                    "middle_flex": 1.08,
                    "ring_flex": 1.08,
                    "little_flex": 1.02,
                },
                "Fingers curled without thumb opposition for carrying handles or bags.",
            ),
            "platform": GraspPose(
                "platform",
                {
                    "thumb_flex": 0.18,
                    "index_flex": 0.05,
                    "middle_flex": 0.05,
                    "ring_flex": 0.05,
                    "little_flex": 0.05,
                },
                "Flat extended-finger support posture for tray or underside support tasks.",
            ),
            "open": GraspPose(
                "open",
                {},
                "Backward-compatible alias for an open relaxed posture.",
            ),
            "pinch": GraspPose(
                "pinch",
                {
                    "thumb_flex": 0.65,
                    "index_flex": 0.7,
                    "middle_flex": 0.12,
                    "ring_flex": 0.08,
                    "little_flex": 0.08,
                },
                "Backward-compatible alias for the precision_pinch grasp.",
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
                "Backward-compatible alias for the cylindrical_power grasp.",
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
