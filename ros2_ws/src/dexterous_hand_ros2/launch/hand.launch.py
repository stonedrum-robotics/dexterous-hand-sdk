"""Launch dexterous hand ROS 2 nodes."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    """Generate the hand node launch description."""
    return LaunchDescription(
        [
            DeclareLaunchArgument("mock", default_value="true"),
            Node(
                package="dexterous_hand_ros2",
                executable="hand_node",
                name="dexterous_hand",
                parameters=[{"mock": True}],
            ),
        ]
    )
