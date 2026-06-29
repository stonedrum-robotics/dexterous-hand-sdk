"""Vendor-neutral quickstart for Linkerbot and AGILINK OmniHand.

This example shows how swapping the driver is the only change needed to move
between hardware vendors. Application logic for grasp sequences, teleoperation,
and data collection can stay identical.

The default ``mock`` backend works without hardware and is safe for CI.
"""

from __future__ import annotations

import argparse

from dexterous_hand import Hand, HandDriver, MockHandDriver
from dexterous_hand.drivers import LinkerbotDriver, OmniHandDriver
from dexterous_hand.drivers.omnihand import OMNIHAND_JOINTS


def build_hand(hardware: str) -> Hand:
    """Construct a :class:`Hand` for the chosen hardware backend."""
    if hardware == "linkerbot":
        driver: HandDriver = LinkerbotDriver(port="/dev/ttyUSB0")
        driver.connect()
        return Hand(driver)
    if hardware == "omnihand":
        driver = OmniHandDriver(host="192.168.1.100")
        driver.connect()
        return Hand(driver)

    driver = MockHandDriver(list(OMNIHAND_JOINTS))
    driver.connect()
    return Hand(driver)


def demo_sequence(hand: Hand) -> None:
    """Read joints, move two fingers, read again, and stop safely."""
    print("Initial joint states:")
    for state in hand.read_joints():
        print(f"  {state.name}: {state.position_rad:.3f} rad")

    print("\nMoving index and middle finger to 30 degrees...")
    hand.move_joints(
        {
            "index_mcp_flex": 0.524,
            "middle_mcp_flex": 0.524,
        }
    )

    print("Joint states after move:")
    for state in hand.read_joints():
        print(f"  {state.name}: {state.position_rad:.3f} rad")

    hand.stop()


def main() -> None:
    """Run the selected backend quickstart."""
    parser = argparse.ArgumentParser(description="Vendor-neutral hand quickstart")
    parser.add_argument(
        "--hardware",
        choices=["mock", "linkerbot", "omnihand"],
        default="mock",
        help="Hardware backend to use.",
    )
    args = parser.parse_args()

    print(f"Connecting to: {args.hardware}")
    hand = build_hand(args.hardware)
    demo_sequence(hand)


if __name__ == "__main__":
    main()
