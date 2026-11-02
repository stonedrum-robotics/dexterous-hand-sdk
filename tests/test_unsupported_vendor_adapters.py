"""Unsupported vendor entry points must reject use without device/network I/O."""

import socket
import sys
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from dexterous_hand import Hand
from dexterous_hand.drivers import LinkerbotDriver, OmniHandDriver


@pytest.fixture
def forbid_transports(monkeypatch):
    serial_open = Mock(side_effect=AssertionError("Serial I/O is forbidden in these tests"))
    tcp_connect = Mock(side_effect=AssertionError("TCP I/O is forbidden in these tests"))
    socket_open = Mock(side_effect=AssertionError("Socket I/O is forbidden in these tests"))
    monkeypatch.setitem(sys.modules, "serial", SimpleNamespace(Serial=serial_open))
    monkeypatch.setattr(socket, "create_connection", tcp_connect)
    monkeypatch.setattr(socket, "socket", socket_open)
    yield serial_open, tcp_connect, socket_open
    for call in (serial_open, tcp_connect, socket_open):
        call.assert_not_called()


@pytest.mark.parametrize("kind", ["linkerbot", "omnihand"])
@pytest.mark.parametrize("operation", ["connect", "read_joints", "command_positions", "stop"])
def test_vendor_operations_reject_without_io(kind, operation, forbid_transports):
    driver = LinkerbotDriver("UNUSED") if kind == "linkerbot" else OmniHandDriver()
    with pytest.raises(NotImplementedError, match="no verified hardware protocol"):
        getattr(driver, operation)(*([{}] if operation == "command_positions" else []))
    driver.disconnect()
    driver.disconnect()


def test_tactile_does_not_return_synthetic_hardware_feedback(forbid_transports):
    with pytest.raises(NotImplementedError, match="no verified hardware protocol"):
        OmniHandDriver().read_tactile()


@pytest.mark.parametrize("kind", ["linkerbot", "omnihand"])
def test_failed_connection_stays_unavailable(kind, forbid_transports):
    driver = LinkerbotDriver("UNUSED") if kind == "linkerbot" else OmniHandDriver()
    for _ in range(2):
        with pytest.raises(NotImplementedError):
            driver.connect()
    hand = Hand(driver)
    with pytest.raises(NotImplementedError):
        hand.move_joints({})
    with pytest.raises(NotImplementedError):
        hand.read_joints()
    with pytest.raises(NotImplementedError):
        hand.stop()


def test_mock_path_remains_in_memory(forbid_transports):
    hand = Hand.mock()
    hand.move_joints({"thumb_flex": 0.25})
    assert {state.name: state.position_rad for state in hand.read_joints()}["thumb_flex"] == 0.25
    hand.open()
    assert all(state.position_rad == 0.0 for state in hand.read_joints())
    hand.stop()


@pytest.mark.parametrize("kind", ["linkerbot", "omnihand"])
@pytest.mark.parametrize("operation", ["open", "stop"])
def test_hand_open_and_stop_reject_unsupported_vendor_without_io(kind, operation, forbid_transports):
    driver = LinkerbotDriver("UNUSED") if kind == "linkerbot" else OmniHandDriver()
    hand = Hand(driver)
    with pytest.raises(NotImplementedError, match="no verified hardware protocol"):
        getattr(hand, operation)()
    driver.disconnect()
