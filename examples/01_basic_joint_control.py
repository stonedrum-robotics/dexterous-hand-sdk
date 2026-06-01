"""Basic joint control example."""

from dexterous_hand import Hand


def main() -> None:
    """Command a mock hand and print joint states."""
    hand = Hand.mock()
    hand.move_joints({"thumb_flex": 0.3, "index_flex": 0.4})
    for state in hand.read_joints():
        print(f"{state.name}: {state.position_rad:.2f} rad")


if __name__ == "__main__":
    main()
