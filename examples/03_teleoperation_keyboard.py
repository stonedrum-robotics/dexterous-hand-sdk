"""Keyboard teleoperation placeholder."""

from dexterous_hand import Hand
from dexterous_hand.teleoperation import TeleoperationController, TeleoperationFrame


def main() -> None:
    """Apply a canned teleoperation frame in mock mode."""
    hand = Hand.mock()
    controller = TeleoperationController(hand)
    controller.apply_frame(TeleoperationFrame({"thumb_flex": 0.5, "index_flex": 0.5}, "keyboard"))
    print("Applied keyboard teleoperation frame")


if __name__ == "__main__":
    main()
