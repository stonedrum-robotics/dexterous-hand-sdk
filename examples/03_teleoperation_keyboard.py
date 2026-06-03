"""Keyboard teleoperation placeholder."""

# Hand provides the command surface; teleoperation maps external inputs into it.
from dexterous_hand import Hand
# A frame is one normalized command packet from a keyboard, glove, or another source.
from dexterous_hand.teleoperation import TeleoperationController, TeleoperationFrame


def main() -> None:
    """Apply a canned teleoperation frame in mock mode."""
    # Mock mode keeps the example deterministic and hardware-free.
    hand = Hand.mock()
    # The controller owns the translation from frames to Hand.move_joints calls.
    controller = TeleoperationController(hand)
    # This canned frame stands in for a keyboard event that curls thumb and index.
    controller.apply_frame(TeleoperationFrame({"thumb_flex": 0.5, "index_flex": 0.5}, "keyboard"))
    # In a real keyboard loop, this print would be replaced by live status feedback.
    print("Applied keyboard teleoperation frame")


# Run the demonstration only when invoked directly from the command line.
if __name__ == "__main__":
    main()
