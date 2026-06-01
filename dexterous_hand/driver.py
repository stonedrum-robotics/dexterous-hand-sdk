"""Hardware driver abstraction for dexterous hands."""

from abc import ABC, abstractmethod

from dexterous_hand.finger import JointState


class HandDriver(ABC):
    """Minimal interface implemented by vendor-specific drivers."""

    @abstractmethod
    def connect(self) -> None:
        """Open communication with the hand."""

    @abstractmethod
    def disconnect(self) -> None:
        """Close communication with the hand."""

    @abstractmethod
    def read_joints(self) -> list[JointState]:
        """Return the current joint states."""

    @abstractmethod
    def command_positions(self, positions_rad: dict[str, float]) -> None:
        """Command target joint positions in radians."""

    @abstractmethod
    def stop(self) -> None:
        """Stop motion immediately where the hardware supports it."""


class MockHandDriver(HandDriver):
    """In-memory driver for tests, demos, and documentation examples."""

    def __init__(self, joint_names: list[str]) -> None:
        self._connected = False
        self._positions = {name: 0.0 for name in joint_names}

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    def read_joints(self) -> list[JointState]:
        self._require_connected()
        return [JointState(name=name, position_rad=value) for name, value in self._positions.items()]

    def command_positions(self, positions_rad: dict[str, float]) -> None:
        self._require_connected()
        unknown = set(positions_rad) - set(self._positions)
        if unknown:
            raise KeyError(f"Unknown joints: {sorted(unknown)}")
        self._positions.update(positions_rad)

    def stop(self) -> None:
        self._require_connected()

    def _require_connected(self) -> None:
        if not self._connected:
            raise RuntimeError("Driver is not connected")
