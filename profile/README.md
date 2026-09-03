# App Brewing Company

This repository holds the organization's **public, static defaults**: the
org profile, community-health files (issue/PR templates, security policy),
and starter workflow templates. It runs **no automation** — no workflows,
no bots, no scheduled jobs.

> **Note:** Most of our work happens in private repositories. This profile
> intentionally shares only what is needed to run the organization — nothing
> about internal projects, roadmaps, or customers appears here.

## What lives here

- `workflow-templates/` — starter workflows repositories can adopt via
  [workflow template options](https://docs.github.com/en/actions/using-workflows/using-starter-workflows-with-your-organization).
  Their reusable implementations live in the org's private governance repo
  and are usable from private org repositories.
- `ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md`, `SECURITY.md` — org-wide
  community defaults.
- `profile/` — this profile.

## Merge policy (org-wide)

- **Squash merges only**; head branches are deleted on merge.
- **PR titles follow [conventional commits](https://www.conventionalcommits.org)**
  (e.g. `feat: add hop selector`, `fix(parser): handle empty input`).
- Reviews and approvals always come from humans.

## Contact

Open an issue in this repository, or reach out to an organization owner.
