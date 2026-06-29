"""Vendor-specific hardware drivers for the Stonedrum Robotics SDK.

Each driver implements :class:`dexterous_hand.driver.HandDriver` and can be
passed to :class:`dexterous_hand.hand.Hand` without any other change to
application code. This is the vendor-neutral guarantee.

Supported hardware
------------------
- :class:`LinkerbotDriver` -- Linkerbot L-series and O-series.
- :class:`OmniHandDriver` -- AGILINK OmniHand series.

Usage example
-------------
>>> from dexterous_hand import Hand
>>> from dexterous_hand.drivers import LinkerbotDriver, OmniHandDriver
>>>
>>> # Swap the driver; the rest of your code is unchanged.
>>> hand = Hand(LinkerbotDriver(port="/dev/ttyUSB0"))
>>> hand = Hand(OmniHandDriver(host="192.168.1.100"))
"""

from dexterous_hand.drivers.linkerbot import LinkerbotDriver
from dexterous_hand.drivers.omnihand import OmniHandDriver, OmniHandConfig, TactileReading

__all__ = ["LinkerbotDriver", "OmniHandConfig", "OmniHandDriver", "TactileReading"]
