"""ROS 2 teleoperation node placeholder."""

try:
    import rclpy
    from rclpy.node import Node
except ImportError:  # pragma: no cover
    rclpy = None
    Node = object


class TeleoperationNode(Node):
    """Receive external teleoperation commands."""

    def __init__(self) -> None:
        super().__init__("dexterous_hand_teleoperation")
        self.get_logger().info("Teleoperation node started")


def main() -> None:
    """Run the teleoperation node."""
    if rclpy is None:
        raise RuntimeError("rclpy is required to run this node")
    rclpy.init()
    node = TeleoperationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
