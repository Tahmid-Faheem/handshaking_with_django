# 🚀 CU-VTS Contribution Workflow — The Bulletproof Guide

> **The only workflow document you need. Follow it every time. Zero rejections.**
>
> Built from **9 real reviewer rejections** across the team. Every rule here exists because someone was rejected for breaking it.

---

## 📑 Table of Contents

1. #-rule-zero--never-do-these-things
2. #-step-0--one-time-machine-setup
3. #-step-1--fork-and-clone-the-repo
4. #-step-2--sync-main-with-upstream
5. #-step-3--create-a-properly-named-branch
6. #-step-4--edit-files-locally-the-right-way
7. #-step-5--self-review-before-committing-critical
8. #-step-6--stage-and-commit-atomically
9. #-step-7--verify-commit-history
10. #-step-8--push-the-branch
11. #-step-9--open-the-pull-request
12. #-step-10--assign-a-reviewer
13. #-step-11--handle-review-feedback
14. #-step-12--after-approval--merge--cleanup
15. #-commit-message-format-conventional-commits
16. #-pr-title--description-template
17. #-markdown-quality-rules-mandatory-for-docs
18. #-common-pitfalls--every-real-failure-mode
19. #-repo-hygiene-files
20. #-final-pre-submission-checklist
21. #-tldr--the-golden-path

---

## 🚨 Rule Zero — Never Do These Things

Every rule below has caused a rejection. Read carefully.

| Never | Why | Rejected in |
|---|---|---|
| Use GitHub's "Upload files" button | Corrupts line endings (CRLF), rewrites entire files | Habib PR #2 |
| Edit files in the GitHub web UI | Same as above | Habib PR #2 |
| Push directly to `main` | Bypasses review + CI | Joy PR #2 |
| Commit without reading `git diff` | Ships typos, blank lines, stray whitespace | All 9 PRs |
| Use CRLF line endings | Rewrites 1000+ lines for a 10-line change | Habib PR #2 |
| Leave HTML template comments (`<!-- ... -->`) in delivered content | Scaffolding must be removed | Tahmid PR #6, Sahil PR #4 |
| Mix commit types in a PR title (e.g., `Feat/docs(prd)`) | Must be one lowercase type | Nayeem PR #5 |
| Hand-wrap Markdown paragraphs at ~80 cols | Creates trailing whitespace, breaks linters | Habib PR #7 |
| Use `*` for bullets | Rest of file uses `-` — must match | Nayeem PR #4 |
| Leave double blank lines or trailing whitespace | Linters and reviewers flag it | Nayeem PR #4, Mohin PR #3, Joy PR #2 |
| Overstate PR wording (e.g., "Implemented" for docs) | Precision matters — say "Defined" or "Documented" | Nayeem PR #5 |
| Push a branch to upstream when you should be on a fork | Standard team etiquette | Tahmid PR #6 |
| Have mismatched Git author name vs GitHub username | Causes attribution confusion in `git log` | Tahmid PR #6 |

---

## 🔧 Step 0 — One-Time Machine Setup

Do this once per computer. Prevents 90% of rejections.

```bash
# 1. Set Git identity — MUST MATCH your GitHub username exactly
git config --global user.name "Tahmid-Faheem"
git config --global user.email "your-github-email@example.com"

# 2. Force LF line endings (prevents Habib-style whole-file rewrites)
git config --global core.autocrlf input

# 3. Auto-set upstream on new branches (skip needing -u)
git config --global push.autoSetupRemote true

# 4. Confirm settings
git config --list | grep -E "user\.name|user\.email|autocrlf|autoSetup"
```

### Editor Configuration

| Editor | Setting to Confirm |
|---|---|
| VS Code | Bottom-right of window shows **LF** (not **CRLF**) |
| VS Code | Install **Code Spell Checker** extension |
| VS Code | Install **markdownlint** extension |
| VS Code | Settings → `"files.trimTrailingWhitespace": true` |
| VS Code | Settings → `"files.insertFinalNewline": true` |
| VS Code | Settings → `"files.eol": "\n"` |

---

## 🔱 Step 1 — Fork and Clone the Repo

**Standard team practice: work from a personal fork, not the upstream.**

```bash
# 1. On GitHub: click "Fork" on the upstream repo
#    → creates https://github.com/<your-username>/Vehicle_Tracking

# 2. Clone YOUR FORK locally
git clone https://github.com/<your-username>/Vehicle_Tracking.git
cd Vehicle_Tracking

# 3. Add upstream as a remote so you can pull the latest main
git remote add upstream https://github.com/azimcs/Vehicle_Tracking.git

# 4. Verify remotes
git remote -v
# Expected:
#   origin    https://github.com/<your-username>/Vehicle_Tracking.git (fetch)
#   origin    https://github.com/<your-username>/Vehicle_Tracking.git (push)
#   upstream  https://github.com/azimcs/Vehicle_Tracking.git (fetch)
#   upstream  https://github.com/azimcs/Vehicle_Tracking.git (push)
```

> **If the team explicitly says "no forks, work on upstream":** skip the fork; clone the upstream directly. Branch naming becomes `docs/prd-section-N` (without your username).

---

## 🔄 Step 2 — Sync Main with Upstream

Always start from an up-to-date `main`. Do this **before every new branch**.

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main         # keeps your fork's main in sync
```

If working directly on upstream (no fork):

```bash
git checkout main
git pull origin main
```

---

## 🌿 Step 3 — Create a Properly Named Branch

### Branch Name Format

**Fork-based workflow:** `<type>/<yourname>/<short-description>`
**Upstream-only workflow:** `<type>/<short-description>`

### Branch Type Reference

| Type | When to Use |
|---|---|
| `docs` | Documentation, PRD, README, reports |
| `feat` | New feature or functionality |
| `fix` | Bug fix |
| `refactor` | Restructuring existing code — **no** behavior change |
| `chore` | Tooling, config, build scripts |
| `test` | Adding or updating tests |

### Examples

```bash
# CASE: Docs work (like PRD section fill-in)
git checkout -b docs/tahmid/prd-section3-personas

# CASE: New backend feature
git checkout -b feat/tahmid/vehicle-model

# CASE: Bug fix
git checkout -b fix/tahmid/dashboard-marker-offset

# CASE: Refactor existing code (no behavior change)
git checkout -b refactor/tahmid/serializer-cleanup

# CASE: Tooling / config
git checkout -b chore/tahmid/add-ruff-config
```

### Verify

```bash
git branch --show-current
```

> ⚠️ If it says `main` — **STOP.** Create a branch immediately.

### Never Use

- ❌ `refactor/...` for **new content** (rejected: Habib PR #2, Tahmid PR #3)
- ❌ `feat/...` for **documentation** (rejected: Nayeem PR #4)
- ❌ Mixed types (e.g., `Feat/docs(prd)...`) — rejected: Nayeem PR #5
- ❌ Capital letters — must be lowercase

---

## ✏️ Step 4 — Edit Files Locally, The Right Way

### Rules

- ✅ Use VS Code / PyCharm / Sublime — **never** GitHub web UI
- ✅ Confirm status bar shows **LF** (not **CRLF**)
- ✅ Enable Code Spell Checker + markdownlint extensions
- ✅ Do **NOT** hand-wrap paragraphs at 80 columns
- ✅ Write **one line per paragraph** in Markdown (linters expect this)
- ✅ Preserve existing structural conventions:
  - Blank line after headings
  - `---` dividers between top-level sections
  - Bullet style matching the rest of the file (`-`, never `*`)

### Fill-In Rules for Templates

When replacing `{{PLACEHOLDER}}` tokens:

1. Replace the placeholder text
2. **Remove any HTML template comments** on the same line (`<!-- Replace {{...}} with ... -->`)
3. **Remove template author guidance comments** (`<!-- e.g. "Reduce time from 30 min to under 5" -->`)
4. Do **not** leave `<!-- ... -->` scaffolding in delivered content

**Rejected examples:**
- Tahmid PR #6: left `<!-- Administrator of the CU Transport Authority -->` inside persona blocks
- Sahil PR #4: left `<!-- Replace {{PROJECT_NAME}} with... -->` after filling the value

### Prose Quality

- Read every sentence out loud once
- Run spell-check
- Split run-on sentences (2–4 short sentences beat one long one)
- Use precise verbs: "Defined admin authentication goal" — **not** "Implemented admin role authentication" (Nayeem PR #5)
- Fix grammar: "has **a** digital way", not "has digital way" (Habib PR #2)
- Use standard English: "shortcomings" or "limitations", **not** "lackings"

---

## 🔍 Step 5 — Self-Review Before Committing (Critical)

**This is where 8 of 9 rejections happened.** Never skip.

```bash
# 1. See what changed
git status

# 2. Confirm line-ending health
git diff --stat
```

> ⚠️ **If a small change shows 1000+ lines modified → STOP.**
> Line endings are corrupted (Habib PR #2 disaster). Do NOT commit.
> Fix with:
> ```bash
> git checkout -- .
> git config core.autocrlf input
> # reopen file in editor, confirm LF at bottom-right, redo edit
> ```

```bash
# 3. Read every changed line
git diff

# 4. Preview Markdown rendering
#    VS Code: Ctrl+Shift+V  (macOS: Cmd+Shift+V)

# 5. Run markdownlint (if editing .md)
markdownlint your-file.md

# 6. Manual whitespace checks
grep -n "  *$" your-file.md              # trailing whitespace
grep -Pzo "\n\n\n" your-file.md          # 3+ consecutive blank lines
grep -n "^\*" your-file.md               # star bullets (should be -)
```

### Required Checks Before Committing

- [ ] `git diff --stat` size matches your intended change (no whole-file blowout)
- [ ] No trailing whitespace on any line
- [ ] No double blank lines
- [ ] All bullets use `-` (matching the file's convention)
- [ ] All `{{PLACEHOLDER}}` tokens replaced
- [ ] All `<!-- template scaffolding comments -->` removed
- [ ] Blank line after every `## Heading`
- [ ] `---` dividers preserved between top-level sections
- [ ] Grammar and spelling checked
- [ ] Markdown preview renders correctly (tables, lists, headings)

---

## 📝 Step 6 — Stage and Commit Atomically

**Rule:** *One reviewable unit = one commit.*

The reviewer explicitly said (Tahmid PR #3):
> *"...atomic separation between 'add personas' and 'add table' as distinct reviewable units."*

Interpret this as: **one commit per named sub-section, not per bullet point.**

### Correct Granularity Examples

| Section | Correct Commits |
|---|---|
| PRD Section 1 (single overview block) | **1 commit** |
| PRD Section 2 (Goals + Non-Goals) | **2 commits** (one per sub-heading) |
| PRD Section 3 (Personas + Role Table) | **2 commits** |
| PRD Section 0 (Title + Owner + Changelog) | **1 commit** (all document control fields) |

### Case A — Edited One Sub-Section

```bash
git add PRD_Vehicle_Tracking.md
git commit -m "docs(prd): add personas to section 3"
```

### Case B — Edited Two Sub-Sections in One Session

Use patch mode to split into two commits:

```bash
git add -p PRD_Vehicle_Tracking.md
```

Git will show each hunk and prompt: `Stage this hunk [y,n,q,a,d,s,e,?]?`

| Key | Action |
|---|---|
| `y` | Include this hunk |
| `n` | Skip this hunk |
| `s` | Split further into smaller hunks |
| `q` | Quit |

**Workflow:**
1. Say `y` to hunks belonging to sub-section 1, `n` to the rest
2. `git commit -m "docs(prd): add personas to section 3"`
3. `git add PRD_Vehicle_Tracking.md` (stages remaining)
4. `git commit -m "docs(prd): add role permission tier table to section 3"`

### Case C — You Already Made One Fat Commit — Split It

```bash
git reset --soft HEAD~1        # keep changes staged, undo the commit
git reset                      # unstage everything
git add -p PRD_Vehicle_Tracking.md
# proceed as Case B
```

### Case D — You Already Made Too Many Tiny Commits — Squash

```bash
git rebase -i HEAD~5           # for last 5 commits
# In the editor:
#   Keep the first line as "pick"
#   Change the rest to "squash" (or "s")
# Save.
# Editor opens again — write the combined commit message.
git push --force-with-lease
```

---

## ✅ Step 7 — Verify Commit History

```bash
git log --oneline
```

**Expected for Section 3:**

```
b2c3d4e docs(prd): add role permission tier table to section 3
a1b2c3d docs(prd): add personas to section 3
```

Clean. Atomic. Spell-checked. One commit per named reviewable unit.

---

## 📤 Step 8 — Push the Branch

### First Push

```bash
git push -u origin docs/tahmid/prd-section3-personas
```

The `-u` sets upstream tracking. Only needed on the first push.

### Subsequent Pushes

```bash
git push
```

### When to Push

- ✅ End of a work session
- ✅ End of the day (for backup)
- ✅ Ready for review
- ❌ Not after every single commit (creates noise)
- ❌ Not if you plan to rewrite history (rebase first, then push)

---

## 🎯 Step 9 — Open the Pull Request

1. Go to **GitHub → your fork**
2. Click the yellow banner **"Compare & pull request"**
   *OR* → **Pull requests** tab → **New pull request**
3. Set direction: **base:** `azimcs/Vehicle_Tracking` `main` ← **compare:** your branch
4. Fill in **title** and **description** using the templates below
5. Assign a reviewer (Step 10)
6. Click **"Create pull request"**

### If Superseding a Previous Rejected PR

Add this line to your PR description:

```
Supersedes #<old-pr-number>
```

Example (Habib PR #7 should have said this about PR #2). Reviewers expect this.

### Draft PRs

If your work isn't ready → dropdown next to "Create pull request" → **"Create draft pull request"**. Convert to "Ready for review" later.

---

## 👥 Step 10 — Assign a Reviewer

### On GitHub

1. Open your PR page
2. Right sidebar → **Reviewers**
3. Search for the teammate's GitHub username
4. Click their name to add them

> ⚠️ **Never leave a PR open without a reviewer** (rejected: Tahmid PR #3, Mohin PR #3).

### Who to Assign

| Scenario | Reviewer |
|---|---|
| Docs / PRD changes | Any active teammate (rotate) |
| Backend Django code | Owner of backend module |
| Frontend / Bootstrap / Leaflet | Owner of frontend module |
| Tooling / config | Team lead or DevOps owner |
| Big architectural change | Team lead + one other |

### For CU-VTS Group 7

- Default reviewer: **@azimcs** (team lead) or **@habiburrahmanakib**
- Rotate reviewers so no one gets overloaded
- **Never merge your own PR** unless explicitly agreed

### After Assigning

Ping in team chat — GitHub notification alone is not enough:

> *"Hey @azimcs, PR #6 for Section 3 is ready for review 🙏"*

---

## 🔁 Step 11 — Handle Review Feedback

```bash
# 1. Make edits in your editor
# ...

# 2. Verify
git diff

# 3. Commit the fix
git add PRD_Vehicle_Tracking.md
git commit -m "docs(prd): address review feedback — remove HTML comments from personas"

# 4. Push
git push
```

### On GitHub

- Reply to **every** review comment:
  - ✅ *"Fixed in `<commit-hash>`"* if you agreed
  - 🤔 Explain respectfully if you disagreed
- Click **"Re-request review"** on the reviewer's avatar in the sidebar

### Engaging With Bots

If the repo has **Copilot Review**, **CodeRabbit**, or similar:

- ✅ Read every bot comment
- ✅ Reply with "Acknowledged" or "Fixed in `<commit>`"
- ✅ Fix genuine issues
- ❌ Never merge while ignoring bot comments (rejected: Joy PR #2)

### Respond Within 24 Hours

If you can't fix it today, at minimum comment saying when you will.

---

## 🎉 Step 12 — After Approval → Merge → Cleanup

### On GitHub

1. Reviewer clicks **"Approve"**
2. Reviewer (or you, if permitted) clicks **"Squash and merge"** or **"Merge pull request"**
3. Delete the branch when GitHub prompts

### Locally

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
git branch -d docs/tahmid/prd-section3-personas
```

---

## ✍️ Commit Message Format (Conventional Commits)

### Structure

```
<type>(<scope>): <short imperative summary>

<optional longer body — explains WHY, not what>

<optional footer — issue references, breaking changes>
```

### Rules for the Summary Line

- ✅ **Lowercase type** (`docs`, never `Docs` or `DOCS`)
- ✅ Present tense, imperative: `add`, not `added` or `adds`
- ✅ Lowercase after the colon
- ✅ **No** trailing period
- ✅ Max 72 characters
- ✅ Spell-check before committing
- ✅ Describe **outcome**, not **implementation** (say "add authentication goal", not "add authentication goal using Django admin")

### ✅ Good Examples (Real Ones From Accepted PRs)

```bash
git commit -m "docs(prd): add personas to section 3"
git commit -m "docs(prd): add role permission tier table to section 3"
git commit -m "docs(prd): fill in section 1 product overview"
git commit -m "docs: fill document control fields in prd"
git commit -m "feat(vehicles): add Vehicle model with plate and owner fields"
git commit -m "fix(dashboard): correct marker placement offset on Leaflet map"
git commit -m "chore(config): configure Ruff linter with project rules"
git commit -m "refactor(views): extract vehicle filtering into helper method"
git commit -m "test(api): add tests for LocationViewSet create endpoint"
```

### ❌ Bad Examples (Real Rejections)

| Message | Why Rejected | Source |
|---|---|---|
| `Targes users` | Typo, vague | Tahmid PR #3 |
| `minetioned` | Typo | Tahmid PR #3 |
| `Add files via upload` | GitHub auto-generated, meaningless | Habib PR #2 |
| `update` | Meaningless | — |
| `final version` | Meaningless | — |
| `Feat/docs(prd): ...` | Mixed types, capitalized | Nayeem PR #5 |

---

## 📋 PR Title & Description Template

**PR Title** = commit-message style:

```
docs(prd): add personas and role permission table to section 3
```

### PR Description Template — Copy This

```markdown
## Summary
One or two sentences describing what this PR does and why.

## Changes
- Concrete bullet list of what changed
- Reference specific files and sections
- Keep factual, not conversational
- Use precise verbs — "Defined", "Documented", "Added"
- Never overstate — "Implemented" is only for actual code

## Verification
Explicit steps the reviewer can follow to confirm this works:
- Docs: "Preview `PRD_Vehicle_Tracking.md` on GitHub 'Files changed' tab"
- Docs: "Confirm the persona blocks and table render correctly"
- Docs: "Confirm `git diff --stat main..HEAD` shows only intended lines changed"
- Code: "Run `python manage.py test <app>` — all tests pass"
- UI:   "Run the server, navigate to /dashboard/, confirm marker appears"

## Related Issue / Task
Closes #<issue-number>
OR: Task: <task name from Group 7 board>

## Supersedes (if applicable)
Supersedes #<old-pr-number>

## Screenshots (if UI)
Paste screenshots here. N/A for docs-only PRs.

## Self-Review Checklist
- [ ] Branch name follows convention (`<type>/<name>/<short-desc>`)
- [ ] Branch type matches the actual change
- [ ] Atomic commits (one logical change each)
- [ ] Commit messages follow Conventional Commits (lowercase type)
- [ ] Commit messages spell-checked
- [ ] `git diff --stat` matches intended scope (no whole-file blowouts)
- [ ] No CRLF line endings
- [ ] No trailing whitespace
- [ ] No double blank lines
- [ ] Bullets use `-` consistently (not `*`)
- [ ] All `{{PLACEHOLDER}}` tokens replaced
- [ ] All template `<!-- comments -->` removed from delivered content
- [ ] Structural conventions preserved (blank lines after headings, `---` dividers)
- [ ] Markdown preview verified
- [ ] `markdownlint` clean (for docs)
- [ ] Reviewer assigned + pinged in chat
- [ ] Related issue linked
```

### Fully-Filled Example (Section 3 Case)

**Title:** `docs(prd): add personas and role permission table to section 3`

**Description:**

```markdown
## Summary
Fills Section 3 (Target Users and Personas) of the CU-VTS PRD by replacing
all placeholder fields with three real personas and a four-role permission
tier table aligned with the mobile-phone-tracker design.

## Changes
- Added three personas to Section 3 of `PRD_Vehicle_Tracking.md`:
  - Mr. Rahman (CU Transport Authority Officer)
  - Karim (Bus Driver)
  - Ms. Nabila (Teacher / Staff Commuter)
- Added a four-role permission tier table:
  - Admin (Transport Authority)
  - Driver
  - Viewer (Teacher / Staff)
  - Superuser (Developer / Maintainer)
- Removed all `{{PERSONA_*}}` and `{{ROLE_*}}` placeholders
- Removed template HTML comments from delivered content

## Verification
- Open `PRD_Vehicle_Tracking.md` in GitHub's rendered view (Files changed tab)
- Confirm all three persona blocks render with headings and bullets
- Confirm the role/permission table renders as a proper Markdown table
- Confirm `git diff --stat main..HEAD` shows a small diff (~50–70 lines)
- No CRLF, no trailing whitespace, no double blank lines

## Related Issue / Task
Task: PRD Section 3 completion — Group 7 sprint 1 board

## Self-Review Checklist
- [x] Branch: `docs/tahmid/prd-section3-personas`
- [x] Two atomic commits (personas + table) — matches reviewer's stated units
- [x] Commit messages follow Conventional Commits (lowercase `docs(prd)`)
- [x] `git diff --stat` verified — only Section 3 area changed
- [x] LF line endings confirmed
- [x] No trailing whitespace or double blank lines
- [x] Bullets use `-`
- [x] All `{{...}}` placeholders replaced
- [x] All `<!-- ... -->` template comments removed
- [x] Structural conventions preserved
- [x] Markdown preview verified locally
- [x] `markdownlint PRD_Vehicle_Tracking.md` clean
- [x] Reviewer requested: @azimcs
```

---

## 🧹 Markdown Quality Rules (Mandatory for Docs)

### Formatting Rules

| Rule | Correct | Wrong | Rejected in |
|---|---|---|---|
| Bullet marker | `- item` | `* item` | Nayeem PR #4 |
| Blank lines between blocks | max **1** | 2 or more | Nayeem PR #4, Mohin PR #3 |
| Trailing whitespace | none | space before newline | Joy PR #2, Habib PR #7 |
| Paragraph wrapping | one line per paragraph | manually wrapped at 80 cols | Habib PR #7 |
| Heading spacing | 1 blank line before + after | none | Habib PR #7 |
| Section dividers | preserve `---` between top-level sections | dropped | Habib PR #7 |
| List indentation | 2 spaces | tabs / 4 spaces | — |

### Install a Markdown Linter (One-Time)

```bash
# CLI:
npm install -g markdownlint-cli
markdownlint PRD_Vehicle_Tracking.md

# VS Code: install the "markdownlint" extension
```

### Manual Whitespace Checks

```bash
# Trailing whitespace on any line
grep -n "  *$" PRD_Vehicle_Tracking.md

# Three or more consecutive blank lines
grep -Pzo "\n\n\n" PRD_Vehicle_Tracking.md

# Star bullets that should be dashes
grep -n "^\*" PRD_Vehicle_Tracking.md
```

Fix any output before committing.

---

## 🚨 Common Pitfalls — Every Real Failure Mode

Every entry here is a real reason a PR was rejected.

### ❌ Line-Ending Corruption

**Symptom:** small edit shows 1000+ lines modified.

```bash
git checkout -- .
git config core.autocrlf input
# Reopen in editor, verify LF at bottom-right, redo edit
```

### ❌ Wrong Branch Type

- `refactor/` is **only** for restructuring existing code — never for new content
- Use `docs/` for documentation, `feat/` for features
- Types must be **lowercase**

### ❌ Committed to Wrong Branch

```bash
git branch temp-fix                    # save current work
git checkout main
git pull upstream main
git checkout -b docs/tahmid/proper-name
git cherry-pick <commit-hash>
git branch -D temp-fix
```

### ❌ Committed to `main` Locally (Not Yet Pushed)

```bash
git branch temp-fix
git reset --hard upstream/main
git checkout -b docs/tahmid/proper-name
git cherry-pick <commit-hash>
git branch -D temp-fix
```

### ❌ Vague / Typo-Ridden Commit Message

```bash
git commit --amend -m "docs(prd): add personas to section 3"
git push --force-with-lease           # only if not merged
```

### ❌ Fat Single Commit Bundling Multiple Units

Split with `git add -p` (Step 6, Case B).

### ❌ Too Many Tiny Commits

Squash with `git rebase -i` (Step 6, Case D).

### ❌ HTML Template Comments Left in Content

Search for and remove them:

```bash
grep -n "<!--" PRD_Vehicle_Tracking.md
```

Delete any lines that are template scaffolding.

### ❌ No Reviewer Assigned

Sidebar → **Reviewers** → add teammate → ping in chat.

### ❌ No PR Description

Never open a PR with a one-line body. Always use the template above.

### ❌ Mismatched Git Author Name vs GitHub Username

```bash
# Fix globally
git config --global user.name "<your-exact-github-username>"

# Fix on past commits (only if not yet merged)
git commit --amend --author="Tahmid-Faheem <email@example.com>" --no-edit
git push --force-with-lease
```

### ❌ Overstated PR Wording

- ❌ "Implemented admin role authentication" (for a docs change)
- ✅ "Defined admin authentication goal"
- ❌ "Built the vehicle tracker"
- ✅ "Documented vehicle tracker requirements"

### ❌ Ignored Bot Review

Reply to every Copilot / CodeRabbit / bot comment. Even "Acknowledged" is enough.

---

## 📁 Repo Hygiene Files

These files should exist in the repo root. If missing, ask the team lead to add them.

### `.gitignore`

```
__pycache__/
*.py[cod]
.venv/
venv/
env/
.env
db.sqlite3
*.log
.DS_Store
.vscode/
.idea/
node_modules/
staticfiles/
media/
```

### `.gitattributes` (Prevents CRLF Disasters)

```
* text=auto eol=lf
*.md text eol=lf
*.py text eol=lf
*.html text eol=lf
*.js text eol=lf
*.css text eol=lf
*.png binary
*.jpg binary
*.pdf binary
```

### `.editorconfig`

```
root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = f*lse
```

### `.markdownlint.json`
*```json
{
  "MD004": { "style": "d*sh" },
  "MD007": { "indent": 2 },
  "MD009": true,
  "MD012": { "maximum": 1 },
  "MD013": false,
  "MD022": true,
  "MD032": true
}
```

### `.github/pull_request_template.md`

Auto-loads the PR template on every new PR. Paste the "PR Description Template" from Step 9 into this file.

---

## ✅ Final Pre-Submission Checklist

Print this. Tape it to your monitor. Run through it before every `git push`.

### Setup
- [ ] Git identity matches GitHub username exactly
- [ ] `core.autocrlf` = `input`
- [ ] Editor set to LF line endings

### Branch
- [ ] Started from up-to-date `main` (fetched from upstream)
- [ ] Working on a fork (not upstream, unless team says otherwise)
- [ ] Branch name: `<type>/<yourname>/<short-desc>`
- [ ] Branch type matches the actual change
- [ ] **Never committed to `main` directly**

### Commits
- [ ] Atomic — one reviewable unit per commit
- [ ] Messages follow Conventional Commits with **lowercase type**
- [ ] Messages spell-checked
- [ ] Precise wording ("Defined", not "Implemented" for docs)

### Content
- [ ] `git diff --stat` matches intended scope
- [ ] No CRLF line endings (LF only)
- [ ] No trailing whitespace
- [ ] No double blank lines
- [ ] Bullets use `-` (matching the file)
- [ ] All `{{...}}` placeholders replaced
- [ ] All template `<!-- ... -->` comments removed
- [ ] Blank line after every heading
- [ ] `---` dividers preserved between top-level sections
- [ ] Paragraphs NOT hand-wrapped at 80 cols
- [ ] Grammar and spelling checked
- [ ] Markdown preview verified
- [ ] `markdownlint` clean

### PR
- [ ] Title follows Conventional Commits style (one lowercase type, no mix)
- [ ] Description filled with full template
- [ ] Verification section lists explicit steps
- [ ] Related issue linked (`Closes #N`)
- [ ] `Supersedes #N` line if this replaces a rejected PR
- [ ] Reviewer assigned + pinged in team chat
- [ ] Automated bot comments (if any) will be acknowledged

---

## ⚡ TL;DR — The Golden Path

```bash
# 1. Sync
git checkout main
git fetch upstream && git merge upstream/main
git push origin main

# 2. Branch (docs, not feat/refactor, for documentation)
git checkout -b docs/tahmid/prd-section3-personas

# 3. Edit locally in VS Code (LF confirmed at bottom-right)
#    - Replace placeholders
#    - Remove template HTML comments
#    - Match bullet style (-)
#    - Preserve structural conventions

# 4. Self-review
git diff --stat
git diff
markdownlint PRD_Vehicle_Tracking.md
grep -n "  *$" PRD_Vehicle_Tracking.md    # trailing whitespace
grep -Pzo "\n\n\n" PRD_Vehicle_Tracking.md # double blank lines
grep -n "<!--" PRD_Vehicle_Tracking.md    # leftover template comments

# 5. Atomic commits (per named sub-section)
git add PRD_Vehicle_Tracking.md
git commit -m "docs(prd): add personas to section 3"

git add PRD_Vehicle_Tracking.md
git commit -m "docs(prd): add role permission tier table to section 3"

# 6. Verify
git log --oneline

# 7. Push
git push -u origin docs/tahmid/prd-section3-personas

# 8. On GitHub:
#    - Open PR against upstream main
#    - Title: docs(prd): add personas and role permission table to section 3
#    - Description: full template (Summary, Changes, Verification, Checklist)
#    - Assign reviewer
#    - Ping reviewer in team chat
#    - If superseding a rejected PR, add "Supersedes #N"
```

---

<div align="center">

## 🎯 The Only Sentence You Need to Remember

**Fork → Sync → Branch correctly → Edit locally in LF → Self-review with `git diff` and `markdownlint` → Commit atomically per named unit → Push → PR with full template → Assign reviewer → Ping in chat → Respond to feedback within 24h.**

---

**Never** use GitHub's "Upload files" button.
**Never** push directly to `main`.
**Never** commit without reading `git diff`.
**Never** leave template `<!-- comments -->` in delivered content.
**Never** open a PR without a reviewer.

---

*This guide was built from 9 real reviewer rejections. Every rule prevents a specific failure that has already happened.*

*Version 2.0 · CU-VTS Group 7 · Bulletproof Edition*

</div>