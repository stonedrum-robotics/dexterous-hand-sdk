"""Tests for the high-level hand API."""

from dexterous_hand import Hand


def test_mock_hand_starts_open(mock_hand: Hand) -> None:
    states = mock_hand.read_joints()
    assert states
    assert all(state.position_rad == 0.0 for state in states)


def test_move_joints_updates_positions(mock_hand: Hand) -> None:
    mock_hand.move_joints({"thumb_flex": 0.25})
    positions = {state.name: state.position_rad for state in mock_hand.read_joints()}
    assert positions["thumb_flex"] == 0.25
