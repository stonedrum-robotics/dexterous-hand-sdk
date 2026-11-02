"""Unsupported vendor adapter interfaces.

These classes retain their names for source compatibility, but all hardware
operations reject use before transport I/O. Use Hand.mock() for in-memory work.
"""

from dexterous_hand.drivers.linkerbot import LinkerbotDriver
from dexterous_hand.drivers.omnihand import OmniHandConfig, OmniHandDriver, TactileReading

__all__ = ["LinkerbotDriver", "OmniHandConfig", "OmniHandDriver", "TactileReading"]
