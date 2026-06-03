"""Run a simple grasp sequence."""

# The Hand class exposes named grasps through its built-in GraspLibrary.
from dexterous_hand import Hand


def main() -> None:
    """Move through open, pinch, cylindrical, and open poses."""
    # Use mock mode first; swap in a hardware driver only after safety checks.
    hand = Hand.mock()
    # The sequence starts and ends open so a demo begins from a safe posture.
    for grasp in ["open", "pinch", "cylindrical", "open"]:
        # Named grasps expand to joint targets inside dexterous_hand/grasp_library.py.
        hand.move_to_grasp(grasp)
        # Printing each step makes the sequence easy to follow in a terminal demo.
        print(f"Applied grasp: {grasp}")


# The guard lets ROS 2 launch files or notebooks import main without side effects.
if __name__ == "__main__":
    main()
