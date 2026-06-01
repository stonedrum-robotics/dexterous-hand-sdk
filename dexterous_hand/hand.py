"""High-level hand API."""

from __future__ import annotations

from dexterous_hand.driver import HandDriver, MockHandDriver
from dexterous_hand.finger import JointState
from dexterous_hand.grasp_library import GraspLibrary


DEFAULT_JOINTS = [
    "thumb_flex",
    "index_flex",
    "middle_flex",
    "ring_flex",
    "little_flex",
]


class Hand:
    """User-facing API for commanding a dexterous hand."""

    def __init__(self, driver: HandDriver, grasp_library: GraspLibrary | None = None) -> None:
        self.driver = driver
        self.grasps = grasp_library or GraspLibrary()

    @classmethod
    def mock(cls) -> "Hand":
        """Create a mock hand suitable for examples and tests."""
        driver = MockHandDriver(DEFAULT_JOINTS)
        driver.connect()
        return cls(driver)

    def read_joints(self) -> list[JointState]:
        """Read current joint states."""
        return self.driver.read_joints()

    def move_joints(self, positions_rad: dict[str, float]) -> None:
        """Move joints to target positions."""
        self.driver.command_positions(positions_rad)

    def move_to_grasp(self, grasp_name: str) -> None:
        """Move to a named grasp pose."""
        pose = self.grasps.get(grasp_name)
        self.move_joints(pose.joint_positions_rad)

    def open(self) -> None:
        """Open the hand to a neutral pose."""
        joints = {state.name: 0.0 for state in self.read_joints()}
        self.move_joints(joints)

    def stop(self) -> None:
        """Stop motion immediately."""
        self.driver.stop()
