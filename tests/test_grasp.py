"""Tests for grasp library integration."""

from dexterous_hand import Hand
from dexterous_hand.grasp_library import GraspLibrary


def test_default_grasp_names() -> None:
    library = GraspLibrary()
    assert "pinch" in library.names()
    assert "cylindrical" in library.names()


def test_move_to_grasp(mock_hand: Hand) -> None:
    mock_hand.move_to_grasp("pinch")
    positions = {state.name: state.position_rad for state in mock_hand.read_joints()}
    assert positions["thumb_flex"] > 0.0
    assert positions["index_flex"] > 0.0
