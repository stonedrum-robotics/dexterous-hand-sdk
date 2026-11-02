"""Unsupported vendor adapter reference.

Joint layouts are unverified draft data. This module implements no vendor
protocol, device feedback, transport, physical stop or compatibility guarantee.
Use Hand.mock() for in-memory examples.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from dexterous_hand.driver import HandDriver
from dexterous_hand.finger import JointState

# Draft reference joint names; not a validated device configuration.
OMNIHAND_JOINTS: list[str] = [
    "thumb_cmc_abd",
    "thumb_cmc_flex",
    "thumb_mcp_flex",
    "thumb_ip_flex",
    "index_mcp_abd",
    "index_mcp_flex",
    "index_pip_flex",
    "index_dip_flex",
    "middle_mcp_flex",
    "middle_pip_flex",
    "middle_dip_flex",
    "ring_mcp_abd",
    "ring_mcp_flex",
    "ring_pip_flex",
    "ring_dip_flex",
    "little_mcp_abd",
    "little_mcp_flex",
    "little_pip_flex",
    "little_dip_flex",
    "wrist_flex",
]

# TODO(WO-13): replace placeholder indices with actual OmniHand register IDs.
JOINT_INDEX: dict[str, int] = {name: i for i, name in enumerate(OMNIHAND_JOINTS)}


@dataclass(frozen=True)
class TactileReading:
    """A single tactile sensor reading from the OmniHand contact layer."""

    sensor_id: int
    force_n: float
    shear_x_n: float = 0.0
    shear_y_n: float = 0.0


@dataclass
class OmniHandConfig:
    """Connection and behaviour configuration for :class:`OmniHandDriver`."""

    host: str = "192.168.1.100"
    port: int = 9090
    timeout: float = 2.0
    joint_names: list[str] = field(default_factory=lambda: list(OMNIHAND_JOINTS))


class OmniHandDriver(HandDriver):
    """Driver stub for AGILINK OmniHand dexterous hands.

    Parameters
    ----------
    host:
        IP address of the OmniHand controller placeholder.
    port:
        TCP port placeholder. AGILINK public material confirms ROS 2 and
        fieldbus interfaces; this value must be confirmed before hardware use.
    config:
        Full configuration object. Overrides *host* and *port* if supplied.
    """

    def __init__(
        self,
        host: str = "192.168.1.100",
        port: int = 9090,
        config: OmniHandConfig | None = None,
    ) -> None:
        self._cfg = config or OmniHandConfig(host=host, port=port)
        self._positions: dict[str, float] = {name: 0.0 for name in self._cfg.joint_names}

    def connect(self) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def disconnect(self) -> None:
        """No transport is opened by this unsupported adapter."""
        return

    def read_joints(self) -> list[JointState]:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def command_positions(self, positions_rad: dict[str, float]) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def stop(self) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def read_tactile(self) -> list[TactileReading]:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def _send_request(self, payload: dict[str, object]) -> dict[str, Any] | None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def _recv_line(self) -> bytes:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def _require_connected(self) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "OmniHandDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def _parse_joint_entries(self, joints: list[object]) -> list[JointState]:
        states: list[JointState] = []
        for entry in joints:
            if not isinstance(entry, dict):
                continue
            joint_id = entry.get("id")
            position = entry.get("position_rad")
            if not isinstance(joint_id, int) or not isinstance(position, int | float):
                continue
            if 0 <= joint_id < len(self._cfg.joint_names):
                states.append(
                    JointState(
                        name=self._cfg.joint_names[joint_id],
                        position_rad=float(position),
                    )
                )
        return states
