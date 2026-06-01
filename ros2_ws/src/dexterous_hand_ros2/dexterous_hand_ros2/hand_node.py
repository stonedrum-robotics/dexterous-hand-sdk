"""ROS 2 node exposing hand joint states and commands."""

from dexterous_hand import Hand

try:
    import rclpy
    from rclpy.node import Node
    from sensor_msgs.msg import JointState
except ImportError:  # pragma: no cover
    rclpy = None
    Node = object
    JointState = object


class HandNode(Node):
    """Publish joint states for a dexterous hand."""

    def __init__(self) -> None:
        super().__init__("dexterous_hand")
        self.hand = Hand.mock()
        self.publisher = self.create_publisher(JointState, "joint_states", 10)
        self.timer = self.create_timer(0.02, self.publish_joint_states)

    def publish_joint_states(self) -> None:
        """Publish current joint states."""
        msg = JointState()
        states = self.hand.read_joints()
        msg.name = [state.name for state in states]
        msg.position = [state.position_rad for state in states]
        msg.velocity = [state.velocity_rad_s for state in states]
        msg.effort = [state.effort_nm for state in states]
        self.publisher.publish(msg)


def main() -> None:
    """Run the ROS 2 hand node."""
    if rclpy is None:
        raise RuntimeError("rclpy is required to run this node")
    rclpy.init()
    node = HandNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
