# .github

Organization-level configuration for **App Brewing Company**.

This repository holds org-wide defaults and shared automation for our GitHub
organization: reusable workflow templates, org-wide community health files,
and maintenance tooling for keeping repositories consistent.

> **Note:** Most of our work happens in private repositories. This profile
> intentionally shares only what is needed to run the organization — nothing
> about internal projects, roadmaps, or customers appears here.

## What lives here

- `workflow-templates/` — starter workflows (CI analysis, release versioning,
  review automation) that repositories can adopt via
  [workflow template options](https://docs.github.com/en/actions/using-workflows/using-starter-workflows-with-your-organization).
- `.github/workflows/` — workflows that keep this repository itself healthy.
- Maintenance scripts for applying workflow and configuration updates across
  the organization's repositories.

## Getting started as a member

- New repositories should copy the relevant templates from
  `workflow-templates/`.
- Squash merges are the org convention; head branches are deleted on merge.
- Automation and agent activity run under the [@appbrew-agent](https://github.com/appbrew-agent)
  account — reviews and merges of its pull requests are handled by the review
  workflow, not by the bot itself.

## Contact

Open an issue in this repository, or reach out to an organization owner.
