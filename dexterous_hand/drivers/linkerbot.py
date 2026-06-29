"""Linkerbot hardware driver for L-series and O-series hands.

Supported products
------------------
- L20 Lite / L20 / L30 -- tendon or linkage-drive research hands.
- O20 / O30 -- direct-drive high-DOF hands.

Communication
-------------
Linkerbot public material lists CAN, RS-485, CAN FD, and ROS support across the
product line. This stub models a serial RS-485 style connection because it is a
portable first integration target for Stonedrum Robotics demos.

Communication implementation is pending vendor API confirmation. Tagged
placeholders identify where Linkerbot-specific protocol bytes will be added
once the vendor interface is available.
"""

from __future__ import annotations

import struct
import time
from typing import TYPE_CHECKING

from dexterous_hand.driver import HandDriver
from dexterous_hand.finger import JointState

if TYPE_CHECKING:
    import serial


# Linkerbot O30: 20 active DOF direct-drive layout.
# Source: project competitive intelligence and Linkerbot ICRA 2026 notes.
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

# Shorter starter layout for L30-style tendon or linkage-drive integrations.
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
        self._serial: serial.Serial | None = None
        self._positions: dict[str, float] = {name: 0.0 for name in self._joint_names}

    def connect(self) -> None:
        """Open the serial connection to the hand."""
        import serial

        self._serial = serial.Serial(
            port=self._port,
            baudrate=self._baud_rate,
            timeout=self._timeout,
        )
        # TODO(WO-13): send Linkerbot initialisation handshake / wake command.
        time.sleep(0.1)

    def disconnect(self) -> None:
        """Close the serial connection."""
        if self._serial and self._serial.is_open:
            # TODO(WO-13): send Linkerbot shutdown / safe-state command.
            self._serial.close()
        self._serial = None

    def read_joints(self) -> list[JointState]:
        """Request and return current joint positions from the hand."""
        self._require_connected()
        # TODO(WO-13): send Linkerbot joint-state request frame and parse bytes.
        return [JointState(name=name, position_rad=pos) for name, pos in self._positions.items()]

    def command_positions(self, positions_rad: dict[str, float]) -> None:
        """Send a joint position command to the hand."""
        self._require_connected()
        unknown = set(positions_rad) - set(self._positions)
        if unknown:
            raise KeyError(f"Unknown joints for Linkerbot: {sorted(unknown)}")

        self._positions.update(positions_rad)
        # TODO(WO-13): encode positions_rad into a Linkerbot binary frame.
        _placeholder_frame = struct.pack(
            f"{len(self._joint_names)}f",
            *(self._positions[name] for name in self._joint_names),
        )

    def stop(self) -> None:
        """Send an immediate-stop command to the hand."""
        self._require_connected()
        # TODO(WO-13): send Linkerbot emergency-stop frame.

    def _require_connected(self) -> None:
        if self._serial is None or not self._serial.is_open:
            raise RuntimeError("LinkerbotDriver is not connected. Call connect() first.")
