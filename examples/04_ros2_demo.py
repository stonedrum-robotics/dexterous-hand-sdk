"""ROS 2 demo launcher notes."""


def main() -> None:
    """Print the ROS 2 launch command for the demo node."""
    # The SDK's ROS 2 package lives under ros2_ws and publishes joint states.
    # Run this command after colcon build and source install/setup.bash.
    print("Run: ros2 launch dexterous_hand_ros2 hand.launch.py mock:=true")


# Keeping this as a plain Python helper makes the launch hint easy to discover.
if __name__ == "__main__":
    main()
