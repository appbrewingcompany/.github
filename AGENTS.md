# AGENTS.md — appbrewingcompany/.github

This repository is the org's PUBLIC defaults home: community-health
defaults (issue/PR templates, SECURITY.md), the org profile, and the
`workflow-templates/` starter UI. It hosts **no runtime automation** —
since the 2026-09-02 migration the live reusable workflows, the seed
flow, the governance skill, and the agent registry live in the org's
PRIVATE runtime repository (callable from private org repos only;
public repos run no org automation and are hand-merged). The starter
templates here point at those private workflows for private repos to
adopt.

Everything here — issues, PR descriptions and comments, commit
messages, release notes, workflow comments, file contents — is visible to
anyone on the internet and indexed by search engines and third-party
mirrors within minutes.

## Disclosure rules for agents (and humans)

Never write org-internal detail into this repo. That includes, without
limitation:

- Authentication architecture: GitHub App names/IDs, token scopes and
  minting flows, secret names, credential-rotation plans.
- Internal repo inventories, dependency graphs between private repos, or
  named private packages.
- Operational practice: runner topology, deployment processes, failure
  post-mortems, migration playbooks, who/what merges when.
- Anything that exists only to coordinate work inside the org.

If a task needs that context to be written down, put it in a private repo,
a local file, or the issue tracker of a private repository — not here.
When linking from this repo to internal context, link to a private
resource (readers without access will simply see a 404) instead of
inlining the content.

Cross-repo migration/tracking issues that list org repos and their CI
states belong in a private ops repo. Issue and PR *comments* can be
hard-deleted; edited *bodies* keep public revision history, and commit
messages are effectively permanent — assume anything written here is
irreversible.

CI workflow YAML necessarily encodes some structure (job names, action
references); that is accepted. Prose descriptions around it are where
leaks happen — describe *what the workflow does*, never *how the org is
organized*.
