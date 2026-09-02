# Organization-level configuration for App Brewing Company

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
- Follow the pull request workflow below — it is enforced by automation on
  every repository.
- Automation and agent activity run under the org's automation accounts —
  reviews and merges of their pull requests are handled by the review
  workflow, not by the bots themselves.

## Pull request workflow

All repositories in the organization follow the same merge policy:

- **Squash merges only.** Rebase and merge-commit methods are disabled at the
  repository level. Each pull request lands on the default branch as exactly
  one commit, and head branches are deleted on merge.
- **The squash commit message is the PR title + PR description** (configured
  per repository), so a clean, conventional-commit history is preserved
  without any intermediate "wip"/"fixup" commits.
- **PR titles must follow [conventional commits](https://www.conventionalcommits.org)** —
  e.g. `feat: add hop selector`, `fix(parser): handle empty input`. Allowed
  types: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`,
  `chore`, `style`, `revert`. The `conventional-pr-title` workflow
  (powered by [amannn/action-semantic-pull-request](https://github.com/amannn/action-semantic-pull-request))
  checks every PR title and fails otherwise.
- **Enforcement** (org is on GitHub Free, so branch protection rules are not
  available for private repos): the `auto-merge` workflow refuses to merge
  any PR with a failing check, which includes the title check. A PR with a
  non-conventional title will not auto-merge until the title is fixed.
  Humans merging manually via the GitHub UI are trusted to respect the red X.

- **Package versioning folds into the merge commit.** In melos repos, the
  `melos-version` workflow versions packages after each single-commit
  (squash-merged) push and amends the version bump and tags directly into
  the merged PR's commit, so releases don't add extra commits to `main`.
  Multi-commit pushes get a separate `ci: version packages` commit.

New repositories created in the org are seeded automatically with the
standard workflows (including `conventional-pr-title`) by the org's
automation.

## Contact

Open an issue in this repository, or reach out to an organization owner.
