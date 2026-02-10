# Gemini Code Duel (v2.4): The Kernel Edition

Turn code hardening into a balanced, zero-sum strategy game.

## 🐧 The Field Judge: "Linus"
In addition to the standard Ruff Referee (who counts Complexity), we now have an **On-Field Judge** enforcing the **Torvalds Standard**.
* **The Philosophy:** "Talk is cheap. Show me the code."
* **The Standard:** Strict, minimal, and precise. (See `ruff.toml`).
* **The Penalty:** Sloppy formatting, unused imports, or messy variables result in **"The Torvalds Tax."**

## ⚖️ The Economy
**Complexity is not free.**
* **Currency:** 1 Token ($\mathcal{S}$) = 1 Cyclomatic Complexity Point (C901).
* **Starting Score:** Both teams start with **100 $\mathcal{S}$**.

### 🔴 Red Team (The Offense)
* **Goal:** Score touchdowns by finding "High Leverage" bugs.
* **Cost:** Pays $\mathcal{S}$ based on **Test Complexity**.
* **Reward:** Refund + 20 $\mathcal{S}$ Bounty if bug found.

### 🔵 Blue Team (The Defense)
* **Goal:** Survival.
* **Cost:** Pays $\mathcal{S}$ based on **Added Complexity**.
* **Reward:** **Refactoring Bonus.** Earn 2 $\mathcal{S}$ per point removed.

---

## 🚩 Penalties & Fouls

### Unnecessary Roughness (Code Golfing)
Merging logic to cheat the bank.
* **The Fine:** Charged full Complexity price + 5 $\mathcal{S}$ Fine.

### Illegal Procedure (Torvalds Tax)
Submitting messy code.
* **Formatting Violation:** 5 $\mathcal{S}$ Fine.
* **Linting Violation (Unused Imports/Vars):** 10 $\mathcal{S}$ Fine.

### Turnover on Downs (Attacker Fails)
If the **Attacker** runs out of tokens:
* **TURNOVER.** Roles are swapped.

### Defensive Collapse (Defender Fails)
If the **Defender** runs out of tokens:
* **INSOLVENCY.** The Defense must delete code to survive.

---

## 🚀 Quick Start
1. `gemini extensions install .`
2. `/harden "Target the memory management module"`
3. `/harden` (The Ref will throw flags for messy code).

## 📂 Files
* `ruff.toml`: The strict "Kernel x ST" configuration file.
* `ADVERSARY.md`: The Scoreboard.
