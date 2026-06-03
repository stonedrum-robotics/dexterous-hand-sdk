"""Tests for teleoperation command mapping."""

import pytest

from dexterous_hand import Hand
from dexterous_hand.teleoperation import TeleoperationController, TeleoperationFrame


def test_apply_frame_moves_hand_joints(mock_hand: Hand) -> None:
    controller = TeleoperationController(mock_hand)

    controller.apply_frame(TeleoperationFrame({"thumb_flex": 0.5}, source="test"))
    positions = {state.name: state.position_rad for state in mock_hand.read_joints()}

    assert positions["thumb_flex"] == 0.5


def test_apply_frame_with_empty_dict_is_no_op(mock_hand: Hand) -> None:
    controller = TeleoperationController(mock_hand)
    before = mock_hand.read_joints()

    controller.apply_frame(TeleoperationFrame({}, source="test"))
    after = mock_hand.read_joints()

    assert after == before


def test_read_glove_frame_raises_not_implemented_error(mock_hand: Hand) -> None:
    controller = TeleoperationController(mock_hand)

    with pytest.raises(NotImplementedError, match="vendor-specific"):
        controller.read_glove_frame()
