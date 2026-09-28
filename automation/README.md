# Automation — waking Claude on Skippy's pushes

`claude-on-skippy-push.yml` is a GitHub Actions workflow. It has to live at
`.github/workflows/claude-on-skippy-push.yml`, but a fine-grained token without the
"Workflows" permission can't push there, so it sits here until Adam moves it.

## Adam's steps (once)
1. On the ThinkPad: install Claude Code, run `claude`, then `/install-github-app`.
   Pick `acwil88/One-square-mile`. It installs the GitHub App and opens a PR with a
   starter `claude.yml` and sets the auth secret. Merge the PR.
2. On github.com, in the repo: Add file → Create new file →
   path `.github/workflows/claude-on-skippy-push.yml` → paste the contents of the
   file next to this README → commit to main.
3. Delete the starter `.github/workflows/claude.yml` if you don't want @claude
   mentions on issues; it's harmless either way.

That's it. The next commit whose message starts with `Skippy` **and contains `[fold]`** wakes Claude, who reads
`CLAUDE.md`, folds the push into the sheet, and pushes back with `[skip ci]`.

## Skippy's side
A cron every 30 minutes: `git pull`; if the newest commit is by Claude and
`SKIPPY-QUEUE.md` gained an item, work it, push with a message starting `Skippy:` — and add `[fold]` to the message **only** when a done-check passed and there is something for Claude to put on the sheet. Never add `[fold]` to a status push. The workflow also refuses to run more than 4 times in 24 hours.

## Cost guards
- Trigger requires `[fold]`, so status pushes cost nothing.
- Hard stop at 4 runs per 24 hours (first step of the workflow).
- Model pinned to Sonnet; 50 turns max; 40-minute timeout; one run at a time.
- If the auth is an API key: set a $20/month spend limit on it in the Anthropic console before merging anything.
