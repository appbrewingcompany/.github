# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| `main` (default branch) | ✅ |
| latest release per repository | ✅ |
| older releases | ❌ |

## Reporting a vulnerability

Report privately to **security@appbrew.co** or, where available, via the
repository's **GitHub Security Advisories** ("Report a vulnerability" in the
Security tab). Please do **not** open a public issue containing vulnerability
details, credentials, customer data, or exploit steps.

We aim to acknowledge reports within **two business days**.

## Scope

- Mobile apps and the packages they depend on
- Org infrastructure and automation surfaces

## Safe-testing boundaries

Security testing is welcome only with explicit written permission from the
owner. Without it, do **not**:

- touch production data or production services
- run destructive actions (deletes, mass mutations, force operations)
- probe for or use leaked credentials
- run load or stress tests

## If a secret was exposed

**Revoke and rotate first, report second.** A leaked key that is revoked
before use is an incident avoided; a reported-but-live key is not.

1. Revoke/rotate the credential everywhere it is valid (GitHub, cloud
   providers, services).
2. Check audit logs for use of the credential since exposure.
3. Then report as above, including scope and rotation status.

## AI agents

AI agents may triage incoming reports and prepare analyses. Only the human
owner decides severity, remediation, and disclosure.

---

This policy is a reporting policy, not a security control.
