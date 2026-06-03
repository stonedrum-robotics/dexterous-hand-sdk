"""Tests for grasp library lookup behavior."""

import pytest

from dexterous_hand.grasp_library import GraspLibrary, GraspPose


def test_all_default_grasp_names_are_present() -> None:
    names = GraspLibrary().names()

    assert len(names) >= 9
    assert {
        "precision_pinch",
        "tripod",
        "lateral_pinch",
        "index_point",
        "cylindrical_power",
        "spherical_power",
        "hook",
        "platform",
        "relaxed_open",
    }.issubset(names)


def test_get_returns_grasp_pose() -> None:
    pose = GraspLibrary().get("tripod")

    assert isinstance(pose, GraspPose)
    assert pose.name == "tripod"


def test_get_raises_key_error_for_unknown_name() -> None:
    with pytest.raises(KeyError, match="unknown"):
        GraspLibrary().get("unknown")


def test_names_returns_sorted_list() -> None:
    names = GraspLibrary().names()

    assert names == sorted(names)


def test_custom_poses_via_constructor() -> None:
    custom_pose = GraspPose(
        "lab_fixture",
        {"thumb_flex": 0.2},
        "Custom pose for a lab fixture.",
    )
    library = GraspLibrary({"lab_fixture": custom_pose})

    assert library.names() == ["lab_fixture"]
    assert library.get("lab_fixture") is custom_pose
