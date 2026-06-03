# Dexterous Hand SDK

[![CI](https://github.com/stonedrum-robotics/dexterous-hand-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/stonedrum-robotics/dexterous-hand-sdk/actions)
[![PyPI](https://img.shields.io/pypi/v/dexterous-hand)](https://pypi.org/project/dexterous-hand/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![ROS 2](https://img.shields.io/badge/ROS%202-Humble%20%7C%20Iron%20%7C%20Jazzy-orange)](https://docs.ros.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](LICENSE)

Vendor-neutral Python & ROS 2 SDK for dexterous robotic hands — mock-mode out of the box, hardware-ready for Linkerbot L20/L30.

## Quick Install

```bash
pip install dexterous-hand
```

For local development:

```bash
python -m pip install -e ".[dev]"
```

## Quick Start

```python
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_joints({"thumb_flex": 0.25, "index_flex": 0.4})

for state in hand.read_joints():
    print(f"{state.name}: {state.position_rad:.2f} rad")

hand.move_to_grasp("precision_pinch")
hand.open()
hand.stop()
```

Run examples from the repository root:

```bash
PYTHONPATH=. python examples/01_basic_joint_control.py
```

## Hardware Compatibility

| Hardware | Interface | Python SDK | ROS 2 | Status |
|---|---|---|---|---|
| Linkerbot L20 Lite | CAN / RS-485 | Planned | Planned | Vendor SDK integration pending |
| Linkerbot L20 | CAN / RS-485 | Planned | Planned | Vendor SDK integration pending |
| Linkerbot L30 | CAN FD | Planned | Planned | Vendor SDK integration pending |
| Mock (simulation) | — | ✅ | ✅ | Ready now |

The mock driver is ready for tests, demos, tutorials, and CI. Physical Linkerbot support depends on vendor SDK access and hardware validation; CE certification remains under verification.

## ROS 2 Quick Start

The ROS 2 package exposes a `dexterous_hand` node that publishes `sensor_msgs/JointState` at 50 Hz in mock mode.

```bash
cd ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch dexterous_hand_ros2 hand.launch.py mock:=true
```

The node follows the current Python mock API:

```python
from dexterous_hand import Hand

hand = Hand.mock()
states = hand.read_joints()
```

## Repository Structure

```text
dexterous-hand-sdk/
├── dexterous_hand/                 # Python SDK package and vendor-neutral API
│   ├── driver.py                   # Hardware abstraction plus MockHandDriver
│   ├── hand.py                     # High-level Hand API used by examples and ROS 2
│   ├── finger.py                   # JointState and Finger validation models
│   ├── grasp_library.py            # Cutkosky-inspired grasp pose library
│   ├── teleoperation.py            # Teleoperation frame and controller interfaces
│   └── utils/                      # Calibration and logging helpers
├── ros2_ws/                        # ROS 2 package, launch file, and node skeletons
├── examples/                       # Runnable mock-mode Python examples
├── tests/                          # Unit tests for SDK behavior
├── docker/                         # Container setup for repeatable development
├── docs/                           # Pointer to the documentation portal
└── .github/                        # CI, release workflows, and issue templates
```

## Documentation

Full documentation is published at <https://stonedrum-robotics.github.io/dexterous-hand-sdk/>.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## Commercial Inquiries

For Linkerbot L20/L30 integration projects, academic demos, training, or procurement questions, contact `info@stonedrum.co`.

## Safety

Always validate joint limits, emergency stop behavior, payload constraints, cable strain relief, and workspace exclusion zones before running against physical hardware.
