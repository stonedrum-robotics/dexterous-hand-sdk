"""AGILINK OmniHand hardware driver.

Supported products
------------------
- OmniHand 3 Ultra-M -- 20 active DOF, 630 g, full direct-drive,
  300+ tactile sensing points, and approximately 0.005 N force resolution.

Communication
-------------
WO-13 found public AGILINK SDK references for C++, Python, ROS 2 wrappers,
CAN FD, RS-485, and EtherCAT. This file keeps a JSON-over-TCP transport as an
unconfirmed integration placeholder until the vendor API is supplied.

DUET architecture
-----------------
AGILINK's DUET (Dual-layer Unified Execution Technology) architecture exposes
two conceptual control loops:
- Operation layer: high-level joint position / velocity commands.
- Contact layer: tactile feedback with approximately 0.005 N force resolution.

Communication implementation is pending vendor API confirmation. Tagged
placeholders identify where AGILINK-specific API details will be added.
"""

from __future__ import annotations

import json
import socket
import time
from dataclasses import dataclass, field
from typing import Any, cast

from dexterous_hand.driver import HandDriver
from dexterous_hand.finger import JointState


# OmniHand 3 Ultra-M: 20 active DOF joint layout.
# Source: AGILINK ICRA 2026 Vienna product presentation, via WO-13.
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
        self._socket: socket.socket | None = None
        self._positions: dict[str, float] = {name: 0.0 for name in self._cfg.joint_names}

    def connect(self) -> None:
        """Open a placeholder TCP connection to the OmniHand controller."""
        self._socket = socket.create_connection(
            (self._cfg.host, self._cfg.port),
            timeout=self._cfg.timeout,
        )
        # TODO(WO-13): send AGILINK session-init message if TCP API is confirmed.
        time.sleep(0.05)

    def disconnect(self) -> None:
        """Close the TCP connection."""
        if self._socket:
            try:
                # TODO(WO-13): send AGILINK session-close message if required.
                self._socket.close()
            except OSError:
                pass
            self._socket = None

    def read_joints(self) -> list[JointState]:
        """Return current joint positions from the OmniHand operation layer."""
        self._require_connected()
        # TODO(WO-13): replace placeholder request with AGILINK ROS 2/API call.
        raw = self._send_request({"cmd": "get_joints"})
        joints = raw.get("joints") if raw else None
        if isinstance(joints, list):
            states = self._parse_joint_entries(joints)
            if states:
                return states

        return [JointState(name=name, position_rad=pos) for name, pos in self._positions.items()]

    def command_positions(self, positions_rad: dict[str, float]) -> None:
        """Send joint position commands to the OmniHand operation layer."""
        self._require_connected()
        unknown = set(positions_rad) - set(self._positions)
        if unknown:
            raise KeyError(f"Unknown joints for OmniHand: {sorted(unknown)}")

        self._positions.update(positions_rad)
        # TODO(WO-13): replace placeholder frame with confirmed AGILINK command.
        payload: dict[str, object] = {
            "cmd": "set_joints",
            "joints": [
                {"id": JOINT_INDEX[name], "position_rad": angle}
                for name, angle in positions_rad.items()
            ],
        }
        self._send_request(payload)

    def stop(self) -> None:
        """Send an emergency-stop command to the OmniHand."""
        self._require_connected()
        # TODO(WO-13): confirm AGILINK stop command or ROS 2 topic.
        self._send_request({"cmd": "stop"})

    def read_tactile(self) -> list[TactileReading]:
        """Return tactile readings from the OmniHand contact layer.

        Full implementation is pending AGILINK API confirmation from vendor
        documentation. Until then, this method returns parsed placeholder
        responses when available and otherwise returns an empty list.
        """
        self._require_connected()
        # TODO(WO-13): replace placeholder request with AGILINK tactile API call.
        raw = self._send_request({"cmd": "get_tactile"})
        sensors = raw.get("sensors") if raw else None
        if not isinstance(sensors, list):
            return []

        readings: list[TactileReading] = []
        for sensor in sensors:
            if not isinstance(sensor, dict):
                continue
            sensor_id = sensor.get("id")
            if not isinstance(sensor_id, int):
                continue
            readings.append(
                TactileReading(
                    sensor_id=sensor_id,
                    force_n=float(sensor.get("fn", 0.0)),
                    shear_x_n=float(sensor.get("fx", 0.0)),
                    shear_y_n=float(sensor.get("fy", 0.0)),
                )
            )
        return readings

    def _send_request(self, payload: dict[str, object]) -> dict[str, Any] | None:
        """Send a JSON placeholder request and return a parsed response."""
        if not self._socket:
            return None
        try:
            message = (json.dumps(payload) + "\n").encode()
            self._socket.sendall(message)
            # TODO(WO-13): confirm framing, likely ROS 2 wrapper rather than TCP JSON.
            response_bytes = self._recv_line()
            if not response_bytes:
                return None
            parsed = json.loads(response_bytes)
            return cast(dict[str, Any], parsed) if isinstance(parsed, dict) else None
        except (OSError, json.JSONDecodeError):
            return None

    def _recv_line(self) -> bytes:
        """Receive bytes until a newline delimiter."""
        if not self._socket:
            return b""
        buffer = b""
        while True:
            chunk = self._socket.recv(4096)
            if not chunk:
                break
            buffer += chunk
            if b"\n" in buffer:
                return buffer.split(b"\n", 1)[0]
        return buffer

    def _require_connected(self) -> None:
        if self._socket is None:
            raise RuntimeError("OmniHandDriver is not connected. Call connect() first.")

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
