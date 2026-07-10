# 🚀 CU-VTS Contribution Workflow

> **Reviewer-proof, professional, always-followable.**
> Follow this every time you contribute. No exceptions.

---

## 📑 Table of Contents

1. #-step-0--one-time-setup-do-once-ever
2. #-step-1--sync-main-with-remote
3. #-step-2--create-a-properly-named-branch
4. #️-step-3--edit-files-locally
5. #-step-4--self-review-before-committing
6. #-step-5--stage-and-commit-atomically
7. #-step-6--verify-commit-history
8. #-step-7--push-the-branch
9. #-step-8--open-the-pull-request
10. #-step-9--assign-a-reviewer
11. #-step-10--handle-review-feedback
12. #-step-11--after-approval--merge--cleanup
13. #️-commit-message-format-conventional-commits
14. #-pr-title--description-template-copy-paste-this
15. #-common-pitfalls-both-failed-prs-hit-these
16. #-repo-hygiene-files-you-must-have
17. #-final-checklist-pin-this
18. #-tldr--the-golden-path

---

## 🔧 Step 0 — One-Time Setup (Do Once, Ever)

Prevents 90% of PR rejections. Run these once per machine.

```bash
# Set your Git identity
git config --global user.name "Tahmid Faheem"
git config --global user.email "your-github-email@example.com"

# Force LF line endings (prevents Habib-style disasters)
git config --global core.autocrlf input

# Optional: skip needing -u for every new branch
git config --global push.autoSetupRemote true

# Verify all settings
git config --list
```

---

## 🔄 Step 1 — Sync Main with Remote

Always start from an up-to-date `main`.

```bash
git checkout main
git pull origin main
```

> ⚠️ **Never** work directly on `main`. Always create a branch (Step 2).

---

## 🌿 Step 2 — Create a Properly Named Branch

**Format:** `<type>/<yourname>/<short-description>`

### Branch Type Reference

| Type | When to Use |
|---|---|
| `docs` | Documentation, PRD, README, reports |
| `feat` | New feature or functionality |
| `fix` | Bug fix |
| `refactor` | Restructuring existing code — **no** behavior change |
| `chore` | Tooling, config, build scripts |
| `test` | Adding or updating tests |

### Examples by Case

```bash
# CASE: Docs work (like PRD Section 3)
git checkout -b docs/tahmid/prd-section3-personas

# CASE: New feature
git checkout -b feat/tahmid/vehicle-model

# CASE: Bug fix
git checkout -b fix/tahmid/dashboard-marker-offset

# CASE: Refactor existing code (no behavior change)
git checkout -b refactor/tahmid/serializer-cleanup

# CASE: Tooling / config
git checkout -b chore/tahmid/add-ruff-config
```

### Verify You're on the New Branch

```bash
git branch --show-current
```

If it says `main` — **STOP.** Create a branch first.

---

## ✏️ Step 3 — Edit Files Locally

### Rules

- ✅ Use VS Code / PyCharm / Sublime — **never** GitHub web UI
- ✅ Confirm bottom-right of VS Code says **LF** (not **CRLF**)
- ✅ Enable a spell-check extension (e.g., Code Spell Checker)

### Never Do This

- ❌ Use GitHub's "Upload files" button
- ❌ Edit directly in the browser
- ❌ Push work without reading the diff

---

## 🔍 Step 4 — Self-Review Before Committing

**This is where BOTH failed PRs went wrong. Never skip this step.**

```bash
# See what changed
git status

# Confirm line-ending health
git diff --stat
# ⚠️ If a small change shows 1000+ lines modified → STOP.
#    Line endings are corrupted. Do NOT commit. Fix first.

# Read every changed line
git diff

# Preview Markdown in VS Code:
#   Windows/Linux: Ctrl + Shift + V
#   macOS:         Cmd + Shift + V
```

### Emergency Fix — Line-Ending Corruption

```bash
git checkout -- .                     # discard local changes
git config core.autocrlf input
# reopen in editor, confirm LF at bottom-right
# redo the edit
```

---

## 📝 Step 5 — Stage and Commit (Atomically)

**Rule:** One logical change per commit.
Personas and permissions table = **2 commits**, not one fat commit.

### Case A — You Edited Only the Personas Section

```bash
git add PRD_Vehicle_Tracking.md
git commit -m "docs(prd): add personas to section 3"
```

### Case B — You Edited Only the Table

```bash
git add PRD_Vehicle_Tracking.md
git commit -m "docs(prd): add role permission tier table to section 3"
```

### Case C — You Edited Both in One Session (Split with Patch Mode)

```bash
git add -p PRD_Vehicle_Tracking.md
```

Git shows each hunk and asks: `Stage this hunk [y,n,q,a,d,s,e,?]?`

| Key | Action |
|---|---|
| `y` | Include this hunk |
| `n` | Skip this hunk |
| `s` | Split further into smaller hunks |
| `q` | Quit |

**Workflow:**
1. Say `y` to personas hunks, `n` to table hunks
2. `git commit -m "docs(prd): add personas to section 3"`
3. `git add PRD_Vehicle_Tracking.md` (stage the rest)
4. `git commit -m "docs(prd): add role permission tier table to section 3"`

---

## ✅ Step 6 — Verify Commit History

```bash
git log --oneline
```

**Expected output:**

```
b2c3d4e docs(prd): add role permission tier table to section 3
a1b2c3d docs(prd): add personas to section 3
```

Clean. Atomic. Spell-checked.

---

## 📤 Step 7 — Push the Branch

### Case: First Push of This Branch

```bash
git push -u origin docs/tahmid/prd-section3-personas
```

The `-u` sets upstream tracking. Only needed on the first push.

### Case: Subsequent Pushes (After Review Feedback)

```bash
git push
```

### When to Push

- ✅ End of a work session
- ✅ End of the day (backup)
- ✅ Finished a subtask
- ✅ Ready for review
- ❌ NOT after every single commit
- ❌ NOT if you plan to rewrite history soon

---

## 🎯 Step 8 — Open the Pull Request

1. Go to **GitHub → your repo**
2. Click the yellow banner **"Compare & pull request"**
   *OR* → **Pull requests** tab → **New pull request**
3. Set: **base:** `main` ← **compare:** `docs/tahmid/prd-section3-personas`
4. Fill in **title** and **description** using the template below (#-pr-title--description-template-copy-paste-this)
5. Assign a reviewer (Step 9)
6. Click **"Create pull request"**

> 💡 If your work isn't ready for review, click the dropdown next to "Create pull request" and choose **"Create draft pull request"** instead.

---

## 👥 Step 9 — Assign a Reviewer

### On GitHub

1. **Open your PR page** on GitHub
2. Right sidebar → **Reviewers**
3. Search for your teammate's GitHub username
4. Click their name to add them
5. GitHub sends them a notification email

### Who to Assign

| Scenario | Reviewer |
|---|---|
| Docs / PRD changes | Any active teammate (rotate) |
| Backend Django code | Owner of backend module |
| Frontend / Bootstrap / Leaflet | Owner of frontend module |
| DevOps / config / CI | Shared M-DEVOPS owner or team lead |
| Big architectural change | Team lead + one other |

### For CU-VTS Group 7

- Default reviewer: **@habiburrahmanakib** or team lead **@azimcs**
- **Rotate** reviewers so no one gets overloaded
- **Never merge your own PR** unless explicitly agreed

### Best Practice

Don't just add the reviewer silently. Ping them in team chat:

> *"Hey @habib, I opened PR #4 for PRD Section 3, would appreciate a review when you have time 🙏"*

---

## 🔁 Step 10 — Handle Review Feedback

```bash
# Reviewer requests changes. You address them:

# 1. Make edits in your editor
# ...

# 2. Verify
git diff

# 3. Commit the fix
git add PRD_Vehicle_Tracking.md
git commit -m "docs(prd): address review feedback — fix typo in Karim persona"

# 4. Push (no -u needed anymore)
git push
```

### On GitHub

- Reply to each review comment:
  - ✅ *"Fixed in `<commit-hash>`"* if you agreed
  - 🤔 Explain respectfully if you disagreed
- Click **"Re-request review"** on the reviewer's avatar in the sidebar

### Respond Within 24 Hours

Don't leave PRs stale. If you can't address it today, comment saying when you will.

---

## 🎉 Step 11 — After Approval → Merge → Cleanup

### On GitHub

1. Reviewer clicks **"Approve"**
2. Click **"Squash and merge"** (recommended default) or **"Merge pull request"**
3. Delete the branch when GitHub prompts you

### Locally

```bash
git checkout main
git pull origin main
git branch -d docs/tahmid/prd-section3-personas   # delete local branch
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

- ✅ Present tense, imperative: `add`, not `added` or `adds`
- ✅ Lowercase after the colon
- ✅ **No** trailing period
- ✅ Max 72 characters
- ✅ **Spell-check before committing**

### ✅ Good Examples

```bash
# Docs
git commit -m "docs(prd): add personas to section 3"
git commit -m "docs(prd): add role permission tier table to section 3"
git commit -m "docs(readme): add installation instructions for local dev"
git commit -m "docs(prd): fix typo in Karim persona description"

# Features
git commit -m "feat(vehicles): add Vehicle model with plate and owner fields"
git commit -m "feat(api): expose LocationViewSet at /api/locations/"
git commit -m "feat(tracker): implement phone GPS reader and POST to backend"
git commit -m "feat(dashboard): render live vehicle marker on Leaflet map"

# Fixes
git commit -m "fix(dashboard): correct marker placement offset on Leaflet map"
git commit -m "fix(api): handle missing timestamp in Location payload"

# Chore
git commit -m "chore(config): configure Ruff linter with project rules"
git commit -m "chore: add gitattributes and editorconfig for LF line endings"

# Refactor
git commit -m "refactor(views): extract vehicle filtering into helper method"

# Tests
git commit -m "test(api): add tests for LocationViewSet create endpoint"
```

### ❌ Bad Examples (Like Both Rejected PRs)

| Message | Problem |
|---|---|
| `Targes users` | Typo + vague |
| `minetioned` | Typo |
| `Add files via upload` | GitHub auto-generated garbage |
| `update` | Meaningless |
| `final version` | Meaningless |
| `fix stuff` | Vague |
| `wip` | Never commit "work in progress" |

---

## 📋 PR Title & Description Template (Copy-Paste This)

Every PR must use this format. No exceptions.

### PR Title

Same style as a commit message:

```
docs(prd): fill in section 3 with personas and permission table
```

### PR Description — Blank Template

Copy this whole block into the PR description box on GitHub:

```markdown
## Summary
One or two sentences describing what this PR does and why.

## Changes
- Concrete bullet list of what changed
- Reference specific files or sections
- Keep it factual, not conversational

## Verification
How the reviewer can confirm this works.
- Docs: "Preview the Markdown on GitHub 'Files changed' tab"
- Code: "Run `python manage.py test vehicles` — all tests should pass"
- UI:   "Run the server, navigate to /dashboard/, confirm marker appears"

## Related Issue / Task
Closes #<issue-number>
OR: Task: <task name from Group 7 board>

## Screenshots (if UI)
Paste screenshots here. N/A for docs-only PRs.

## Checklist
- [ ] Branch name follows convention (`<type>/<name>/<short-desc>`)
- [ ] Commit messages follow Conventional Commits
- [ ] `git diff --stat` shows only intended changes (no line-ending noise)
- [ ] Spell-checked
- [ ] Markdown preview verified (for docs)
- [ ] Ran linter locally (for code): `ruff check .`
- [ ] Reviewer requested
- [ ] Related issue linked
```

### PR Description — Fully Filled Example (Your PRD Case)

**Title:**

```
docs(prd): fill in section 3 with personas and permission table
```

**Description:**

```markdown
## Summary
Fills in Section 3 (Target Users and Personas) of the CU-VTS PRD by replacing
all placeholder fields with three real personas and a four-role permission tier
table aligned with the mobile-phone-tracker design.

## Changes
- Added three personas to `PRD_Vehicle_Tracking.md` Section 3:
  - Mr. Rahman (CU Transport Authority Officer)
  - Karim (Bus Driver)
  - Ms. Nabila (Teacher / Staff Commuter)
- Added a 4-role permission tier table:
  - Admin (Transport Authority)
  - Driver
  - Viewer (Teacher / Staff)
  - Superuser (Developer / Maintainer)
- Removed all `{{PERSONA_*}}` and `{{ROLE_*}}` placeholders

## Verification
- Open `PRD_Vehicle_Tracking.md` in GitHub's rendered view (Files changed tab)
- Confirm all three persona blocks render with headings and bullets
- Confirm the role/permission table renders as a proper Markdown table
- Confirm `git diff --stat main..HEAD` shows only Section 3 area changed
  (should be ~50–70 line change, no line-ending noise)

## Related Issue / Task
Task: PRD Section 3 completion — Group 7 sprint 1 board

## Checklist
- [x] Branch: `docs/tahmid/prd-section3-personas`
- [x] Two atomic commits following Conventional Commits
- [x] `git diff --stat` verified — only Section 3 area changed
- [x] Spell-checked with VS Code extension
- [x] Markdown preview verified locally
- [x] Reviewer requested: @habiburrahmanakib
```

---

## 🚨 Common Pitfalls (Both Failed PRs Hit These)

### ❌ Line-Ending Corruption

**Symptom:** small edit shows massive diff (1000+ lines).

```bash
git checkout -- .
# reopen in editor, ensure LF at bottom-right
# redo the edit
```

### ❌ Wrong Branch Type

**Symptom:** Branch named `refactor/` but you're adding new content.
Use `docs/` for documentation, `feat/` for new features. `refactor/` is ONLY for restructuring existing code without behavior change.

### ❌ Committed to Wrong Branch

```bash
git branch temp-fix                   # save current work
git checkout main
git pull
git checkout -b docs/tahmid/proper-name
git cherry-pick <commit-hash>
git branch -D temp-fix
```

### ❌ Fat Single Commit

Split with `git add -p` (see Step 5 Case C).

### ❌ Vague Commit Message

```bash
git commit --amend -m "docs(prd): add personas to section 3"
git push --force-with-lease    # only if not merged yet
```

### ❌ No Reviewer Assigned

Sidebar → Reviewers → add teammate → also ping in chat.

### ❌ Pushed to `main` by Accident

Immediately stop. Do not push more. Notify team lead. Revert may be needed.

---

## 📁 Repo Hygiene Files (You Must Have)

### `.gitignore` — Never Commit These

```
__pycache__/
*.py[cod]
.venv/
venv/
env/
.env
db*sqlite3
*.log
.DS_Store
.vscode/
.*dea/
node_modules/
staticfiles/
me*ia/
```

### `.gitattributes` — En*orce LF for Everyone

```** text=auto eol=lf
*.md text eol=l*
*.py text eol=lf
*.html text eol=*f
*.js text eol=lf
*.css text eol=*f
*.png binary
*.jpg binary
*.pdf *inary
```

### Final Sanity Checks*Before Every PR

```bash
git*log --oneline main..HEAD          * only your intended commits?
git d*ff --stat main..HEAD            # *nly intended files?
git status    *                        # nothing *ncommitted?
```

---

## ✅ Final C*ecklist (Pin This)

Before you cli*k **"Create pull request"**, tick *very box mentally:

- [ ] Started *rom up-to-date `main`
- [ ] Branch*named: `<type>/<yourname>/<short-d*sc>`
- [ ] Branch type matches the*actual change
- [ ] Atomic commits*(one logical change each)
- [ ] Co*mit messages follow Conventional C*mmits
- [ ] Commit messages are sp*ll-checked
- [ ] `git diff --stat`*shows only intended changes
- [ ] *o line-ending corruption (LF confi*med)
- [ ] Ran spell-check on file*content
- [ ] Ran Markdown preview*if editing `.md`
- [ ] Ran linter *for code): `ruff check .`
- [ ] `.*itignore` respected (no `db.sqlite*`, `__pycache__`, `.env`)
- [ ] PR*title follows commit style
- [ ] P* description filled with template
* [ ] Reviewer assigned + pinged in*chat
- [ ] Related issue linked (`*loses #N`)

---

## ⚡ TL;DR — The *olden Path

```bash
# 1. Start cle*n
git checkout main && git pull or*gin main

# 2. Branch properly
git*checkout -b docs/tahmid/prd-sectio*3-personas

# 3. Edit locally, sel*-review
git diff --stat &&*git diff

# 4. Atomic commits
git *dd PRD_Vehicle_Tracking.md
git com*it -m "docs(prd): add personas to *ection 3"

git add PRD_V*hicle_Tracking.md
git commit -m "d*cs(prd): add role permission tier *able to section 3"

# 5. Verify + *ush
git log --oneline
git push -u *rigin docs/tahmid/prd-section3-per*onas

# 6. On GitHub:
#    - Fill *R title + description using templa*e
#    - Assign reviewer
#    - Pi*g reviewer in team chat
```

**Fol*ow this every time. Zero rejection*. Reviewer-proof.**

---

<div ali*n="center">

### 🎯 The Golden Rul*

**Clone → Branch → Edit locally * Self-review → Commit atomically →*Push at checkpoints → PR with temp*ate → Assign reviewer → Ping in ch*t**

**Never** use GitHub's "Uploa* files" button.
**Never** edit dir*ctly on the web UI.
**Never** push*without reading `git diff`.

*Last*updated: v1.0 — CU-VTS Group 7*

<*div>
