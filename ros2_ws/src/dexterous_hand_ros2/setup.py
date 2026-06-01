"""ROS 2 package setup."""

from setuptools import setup

package_name = "dexterous_hand_ros2"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
        (f"share/{package_name}/launch", ["launch/hand.launch.py"]),
        (f"share/{package_name}/config", ["config/default.yaml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Stonedrum Robotics",
    maintainer_email="info@stonedrum.co",
    description="ROS 2 nodes for dexterous hand control.",
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "hand_node = dexterous_hand_ros2.hand_node:main",
            "teleoperation_node = dexterous_hand_ros2.teleoperation_node:main",
            "grasp_action_server = dexterous_hand_ros2.grasp_action_server:main",
        ],
    },
)
