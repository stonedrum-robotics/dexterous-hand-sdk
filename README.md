# Dexterous Hand SDK

Python hand-interface reference code with an in-memory mock driver. Use it to explore joint commands, joint-state objects and scripted mock grasp poses without connecting a device.

## Current scope

- `Hand.mock()` stores and returns joint positions in memory.
- Linkerbot and OmniHand classes are unsupported adapter placeholders. Their hardware operations raise `NotImplementedError` before opening a transport or sending commands.
- The mock is not a physics simulator. ROS 2, MuJoCo, MoveIt and physical-device compatibility are not established by the Python mock example.

## Try the in-memory API

From this source checkout with Python 3.10 or newer:

```bash
PYTHONPATH=. python3 - <<'PYTHON'
from dexterous_hand import Hand

hand = Hand.mock()
hand.move_joints({"thumb_flex": 0.25, "index_flex": 0.4})
for state in hand.read_joints():
    print(f"{state.name}: {state.position_rad:.2f} rad")
hand.open()
hand.stop()
PYTHON
```

Expected joint-state output:

```text
thumb_flex: 0.25 rad
index_flex: 0.40 rad
middle_flex: 0.00 rad
ring_flex: 0.00 rad
little_flex: 0.00 rad
```

`open()` sets the mock's positions to zero. `stop()` on the mock performs no physical action. The source contains no qualified emergency-stop implementation for a real hand.

## Repository contents

| Path | Scope |
|---|---|
| `dexterous_hand/` | Python interfaces, in-memory mock, grasp data and unsupported vendor placeholders |
| `examples/` | Python examples; inspect each example's backend and prerequisites |
| `tests/` | Unit tests and checks that unsupported vendor paths reject operation |
| `ros2_ws/` | ROS 2 integration source requiring its own environment and verification |
| `docker/` | Development configuration requiring its own build verification |

The [legacy documentation](https://stonedrum-robotics.github.io/docs/) contains broader historical material. It is not evidence of current hardware or integration support. Current changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Contributing and enquiries

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance. For a scoped component or integration discussion, contact [info@stonedrum.co](mailto:info@stonedrum.co).
