"""Tests for the mock hand driver."""

import pytest

from dexterous_hand.driver import MockHandDriver


def test_connect_disconnect_state() -> None:
    driver = MockHandDriver(["thumb_flex"])
    driver.connect()
    driver.disconnect()

    with pytest.raises(RuntimeError, match="not connected"):
        driver.read_joints()


def test_command_positions_updates_state() -> None:
    driver = MockHandDriver(["thumb_flex", "index_flex"])
    driver.connect()

    driver.command_positions({"thumb_flex": 0.42})
    positions = {state.name: state.position_rad for state in driver.read_joints()}

    assert positions["thumb_flex"] == 0.42
    assert positions["index_flex"] == 0.0


def test_read_joints_returns_correct_joint_state_list() -> None:
    driver = MockHandDriver(["thumb_flex", "index_flex"])
    driver.connect()

    states = driver.read_joints()

    assert [state.name for state in states] == ["thumb_flex", "index_flex"]
    assert [state.position_rad for state in states] == [0.0, 0.0]


def test_command_positions_raises_key_error_for_unknown_joint() -> None:
    driver = MockHandDriver(["thumb_flex"])
    driver.connect()

    with pytest.raises(KeyError, match="missing_flex"):
        driver.command_positions({"missing_flex": 0.1})


@pytest.mark.parametrize("operation", ["read", "command", "stop"])
def test_operations_raise_runtime_error_when_not_connected(operation: str) -> None:
    driver = MockHandDriver(["thumb_flex"])

    with pytest.raises(RuntimeError, match="not connected"):
        if operation == "read":
            driver.read_joints()
        elif operation == "command":
            driver.command_positions({"thumb_flex": 0.1})
        else:
            driver.stop()
