"""Unsupported vendor adapter reference.

Joint layouts are unverified draft data. This module implements no vendor
protocol, device feedback, transport, physical stop or compatibility guarantee.
Use Hand.mock() for in-memory examples.
"""

from __future__ import annotations

from dexterous_hand.driver import HandDriver
from dexterous_hand.finger import JointState

# Draft reference joint names; not a validated device configuration.
LINKERBOT_O30_JOINTS: list[str] = [
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

# Draft shorter reference layout; not a validated device configuration.
LINKERBOT_L30_JOINTS: list[str] = [
    "thumb_flex",
    "thumb_abd",
    "index_flex",
    "middle_flex",
    "ring_flex",
    "little_flex",
]


class LinkerbotDriver(HandDriver):
    """Driver stub for Linkerbot L-series and O-series dexterous hands.

    Parameters
    ----------
    port:
        Serial port path, for example ``/dev/ttyUSB0`` on Linux or ``COM3`` on
        Windows.
    baud_rate:
        Serial baud rate. The default placeholder is 115 200 baud.
    joint_names:
        Ordered joint names. Defaults to :data:`LINKERBOT_O30_JOINTS`; pass
        :data:`LINKERBOT_L30_JOINTS` for the shorter L-series starter layout.
    timeout:
        Read timeout in seconds.
    """

    def __init__(
        self,
        port: str,
        baud_rate: int = 115_200,
        joint_names: list[str] | None = None,
        timeout: float = 1.0,
    ) -> None:
        self._port = port
        self._baud_rate = baud_rate
        self._joint_names = joint_names or list(LINKERBOT_O30_JOINTS)
        self._timeout = timeout
        self._positions: dict[str, float] = {name: 0.0 for name in self._joint_names}

    def connect(self) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "LinkerbotDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def disconnect(self) -> None:
        """No transport is opened by this unsupported adapter."""
        return

    def read_joints(self) -> list[JointState]:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "LinkerbotDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def command_positions(self, positions_rad: dict[str, float]) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "LinkerbotDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )

    def stop(self) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "LinkerbotDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )
        # TODO(WO-13): send Linkerbot emergency-stop frame.

    def _require_connected(self) -> None:
        """Reject unsupported hardware operation before any I/O."""
        raise NotImplementedError(
            "LinkerbotDriver has no verified hardware protocol. "
            "Use Hand.mock() for in-memory examples."
        )
