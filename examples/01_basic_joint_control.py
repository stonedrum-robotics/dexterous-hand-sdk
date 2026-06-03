"""Basic joint control example."""

# Import the high-level API; it hides the concrete driver implementation.
from dexterous_hand import Hand


def main() -> None:
    """Command a mock hand and print joint states."""
    # Mock mode connects an in-memory driver, so this example is safe in CI.
    hand = Hand.mock()
    # Command two joints in radians; unspecified joints keep their last value.
    hand.move_joints({"thumb_flex": 0.3, "index_flex": 0.4})
    # Read back every joint state to confirm the command reached the driver.
    for state in hand.read_joints():
        # Print compact telemetry that mirrors what a ROS JointState would carry.
        print(f"{state.name}: {state.position_rad:.2f} rad")


# Keep the example importable by tests while still runnable as a script.
if __name__ == "__main__":
    main()
