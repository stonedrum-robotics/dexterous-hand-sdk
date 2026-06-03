# Security Policy

## Supported Versions

Security updates are provided for the latest released version of public SDK packages, ROS 2 examples, and documentation. If you are using an older commit for a lab integration, include the exact commit SHA in your report so maintainers can assess whether the issue still applies.

## Responsible Disclosure

Please report suspected vulnerabilities privately to `info@stonedrum.co`. Do not open a public issue for vulnerabilities, command-injection paths, unsafe motion triggers, or limit-bypass behavior until maintainers have reviewed the report.

Include:

- Affected repository, package version, and commit SHA.
- Affected hand model, simulator, or mock-mode path.
- Operating system, Python version, and ROS 2 distribution.
- Description of the vulnerability or unsafe behavior.
- Reproduction steps with the smallest possible script, launch file, or log.
- Expected impact, including whether physical motion, data exposure, or denial of service is possible.
- Any suggested mitigation.

## Response SLA

We aim to acknowledge security reports within 72 hours. After acknowledgement, maintainers will triage severity, ask for any missing reproduction details, and coordinate a fix or mitigation plan before public disclosure.

## Hardware Safety Issues

Reports involving unexpected physical motion, emergency-stop bypass, joint-limit bypass, unsafe calibration, or command execution from untrusted input are treated as security and safety issues. Include whether the behavior was observed on real hardware or in mock/simulation mode.

## Disclosure Timeline

Please give maintainers a reasonable remediation window before public disclosure. If the issue is actively exploited or creates immediate physical risk, state that clearly in the first email subject line.
