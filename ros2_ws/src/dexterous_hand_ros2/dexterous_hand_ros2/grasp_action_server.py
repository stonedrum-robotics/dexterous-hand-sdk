"""ROS 2 grasp action server placeholder."""

try:
    import rclpy
    from rclpy.node import Node
except ImportError:  # pragma: no cover
    rclpy = None
    Node = object


class GraspActionServer(Node):
    """Execute named grasp requests."""

    def __init__(self) -> None:
        super().__init__("dexterous_hand_grasp_action_server")
        self.get_logger().info("Grasp action server placeholder started")


def main() -> None:
    """Run the grasp action server."""
    if rclpy is None:
        raise RuntimeError("rclpy is required to run this node")
    rclpy.init()
    node = GraspActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
