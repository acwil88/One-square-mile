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

That's it. The next commit whose message starts with `Skippy` wakes Claude, who reads
`CLAUDE.md`, folds the push into the sheet, and pushes back with `[skip ci]`.

## Skippy's side
A cron every 30 minutes: `git pull`; if the newest commit is by Claude and
`SKIPPY-QUEUE.md` gained an item, work it, push with a message starting `Skippy:`.
