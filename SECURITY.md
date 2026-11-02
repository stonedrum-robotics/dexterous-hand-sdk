# Security Policy

## Scope and supported code

This policy covers the code, examples and documentation in the Stonedrum Robotics public repositories, which are early-stage mock-mode and reference material. Only the current `main` branch of each repository is considered for fixes. Maintenance of earlier commits, releases or forks is not promised. If you are running an older commit, include its SHA in your report.

## Reporting a vulnerability

Please report suspected vulnerabilities privately by email to `info@stonedrum.co`, starting the subject line with `Security:`. This is the general contact for Stonedrum Robotics; no response time is published.

Do not open a public issue or pull request for vulnerabilities, command-injection paths, unsafe-motion triggers or limit-bypass behaviour until the report has been reviewed and a way forward has been agreed.

Please include:

- The affected repository, package version and commit SHA.
- The affected component, and whether it was mock mode, a simulator or other hardware or software.
- Operating system, Python version and, if relevant, ROS 2 distribution.
- A description of the vulnerability or unsafe behaviour.
- The smallest reproduction you can give: script, launch file or trimmed output.
- The impact you expect, such as unexpected motion, data exposure or denial of service.
- Any mitigation you suggest.

Please do not send credentials, tokens, customer or supplier data, private logs or recordings. Redact them before sending.

## What to expect

Maintainers may ask for further detail. No acknowledgement or fix timeline is published, and none is guaranteed. If you plan to disclose publicly, please say so in your first message and allow reasonable time for a response.

## Physical-safety concerns

If equipment or people may be at immediate risk, stop operation and follow the equipment manufacturer's emergency-stop and safety procedures first. Email is not an emergency channel. Software behaviour that could cause unexpected motion, or that bypasses limits, can still be reported through the private route above. Say whether you saw it in mock mode, in simulation or on real hardware. These repositories do not establish hardware integration unless a repository README says so.
