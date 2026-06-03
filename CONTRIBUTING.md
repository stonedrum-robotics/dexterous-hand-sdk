# Contributing

Thanks for helping improve Stonedrum Robotics open-source dexterous-hand tooling. These repositories support researchers and engineers integrating dexterous robotic hands with Python, ROS 2, simulation, and lab hardware.

## Issue Reporting

Use GitHub Issues for reproducible bugs, missing documentation, integration problems, and feature requests.

For bugs, include:

- Repository name and SDK version or commit SHA.
- Operating system, Python version, and ROS 2 distribution.
- Hand model or mock mode.
- Minimal code, launch command, or log output that reproduces the issue.
- Expected behavior and actual behavior.
- Any safety-relevant context, such as unexpected motion or limit handling.

For feature requests, include:

- The use case and target user.
- The hand model, robot arm, simulator, or ROS 2 package involved.
- A proposed API or workflow if you already have one.
- Whether you are willing to test or contribute the change.

## Pull Request Process

1. Fork the relevant repository.
2. Create a focused branch from `main`.
3. Make the smallest coherent change that solves the issue.
4. Add or update tests for new behavior.
5. Run local checks before opening a pull request.
6. Open a pull request against `main` with a clear summary and test notes.

Accepted branch prefixes:

- `fix/` for bug fixes.
- `feat/` for new features.
- `docs/` for documentation updates.
- `chore/` for maintenance, dependency, or workflow changes.

## Code Standards

- Python code must pass `ruff check .`.
- Python code must pass `mypy dexterous_hand` with strict type checking.
- Public functions, classes, and methods must have docstrings and type hints.
- Public APIs should remain vendor-neutral unless the change is explicitly a vendor adapter.
- Hardware-facing code must fail safely, document assumptions, and avoid silent limit bypasses.
- Examples should run in mock mode whenever possible so they are useful without hardware.

## Test Requirements

New code must include tests. For SDK changes, prefer small unit tests under `tests/` that run without physical hardware. For ROS 2 or hardware integration changes, include a mock-mode test, a manual verification checklist, or both.

Run:

```bash
ruff check .
mypy dexterous_hand
pytest
```

## Commit Message Format

Use Conventional Commits:

```text
feat: add tripod grasp preset
fix: validate unknown joint names in mock driver
docs: expand UR integration checklist
chore: update CI Python matrix
```

Use `feat`, `fix`, `docs`, `test`, `refactor`, `build`, `ci`, or `chore` as the type. Keep the subject concise and explain hardware or safety implications in the body when relevant.
