"""Run a simple grasp sequence."""

from dexterous_hand import Hand


def main() -> None:
    """Move through open, pinch, cylindrical, and open poses."""
    hand = Hand.mock()
    for grasp in ["open", "pinch", "cylindrical", "open"]:
        hand.move_to_grasp(grasp)
        print(f"Applied grasp: {grasp}")


if __name__ == "__main__":
    main()
