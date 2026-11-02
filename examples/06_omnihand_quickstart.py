"""Synthetic in-memory sequence using draft joint names.

Only the mock backend is implemented; vendor names are not compatibility claims.
"""

from __future__ import annotations

import argparse

from dexterous_hand import Hand, MockHandDriver
from dexterous_hand.drivers.omnihand import OMNIHAND_JOINTS


def build_hand(hardware: str) -> Hand:
    """Construct a synthetic mock; reject unsupported physical backends."""
    if hardware != "mock":
        raise NotImplementedError("Only the mock backend is implemented; no device was opened.")
    driver = MockHandDriver(list(OMNIHAND_JOINTS))
    driver.connect()
    return Hand(driver)


def demo_sequence(hand: Hand) -> None:
    """Read and update synthetic joint positions, then finish the mock sequence."""
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
    parser = argparse.ArgumentParser(description="In-memory mock hand example")
    parser.add_argument(
        "--hardware",
        choices=["mock", "linkerbot", "omnihand"],
        default="mock",
        help="Hardware backend to use.",
    )
    args = parser.parse_args()
    if args.hardware != "mock":
        parser.error("Only mock is implemented; vendor adapters have no verified hardware protocol.")

    print(f"Backend: {args.hardware} (in memory)")
    hand = build_hand(args.hardware)
    demo_sequence(hand)


if __name__ == "__main__":
    main()
