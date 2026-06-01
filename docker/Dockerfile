FROM ros:humble-ros-base

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace/dexterous-hand-sdk
COPY . .

RUN python3 -m pip install --upgrade pip && python3 -m pip install -e ".[dev]"

ENTRYPOINT ["/bin/bash"]
