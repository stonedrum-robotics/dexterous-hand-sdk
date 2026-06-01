# Dexterous Hand SDK

Python and ROS 2 tooling for dexterous robotic hands, designed around a vendor-neutral hardware abstraction layer.

## Status

This repository is an implementation scaffold. It includes typed interfaces, examples, ROS 2 node skeletons, tests, Docker setup, and CI workflows.

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Python quick start

```python
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_to_grasp("pinch")
hand.open()
```

Run examples from the repository root:

```bash
PYTHONPATH=. python examples/01_basic_joint_control.py
```

## ROS 2 quick start

```bash
ros2 launch dexterous_hand_ros2 hand.launch.py mock:=true
```

## Safety

Always validate joint limits, emergency stop behavior, and payload constraints before running against physical hardware.
