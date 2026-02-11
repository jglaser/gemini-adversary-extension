# Gemini Code Duel (v2.5): The Equilibrium Edition ⚖️

Turn code hardening into a balanced, zero-sum strategy game.

Previous versions suffered from the "Defender's Dilemma" (bleeding tokens to fix bugs). Version 2.5 introduces **Detailed Balance**: The complexity of the attack now funds the complexity of the defense.

## 🐧 The Field Judge: "Linus"
In addition to the standard Ruff Referee (who counts Complexity), we have an **On-Field Judge** enforcing the **Torvalds Standard**.
* **The Philosophy:** "Talk is cheap. Show me the code."
* **The Standard:** Strict, minimal, and precise. (See `ruff.toml`).
* **The Penalty:** Sloppy formatting, unused imports, or messy variables result in **"The Torvalds Tax."**

## ⚖️ The Economy (Conservation of Complexity)
**Complexity is not free.**
* **Currency:** 1 Token ($\mathcal{S}$) = 1 Cyclomatic Complexity Point (C901).
* **Starting Score:** Both teams start with **100 $\mathcal{S}$**.

### The "Energy Transfer" Rule (New in v2.5)
To prevent the Defense from going bankrupt fixing complex bugs:
* **The Grant:** When the Red Team finds a bug with a test of Complexity $k$, that $k$ is **transferred** to the Blue Team.
* **The Logic:** A complex attack requires a complex defense. The Red Team inadvertently funds the patch.

### 🔴 Red Team (The Offense)
* **Goal:** Score touchdowns by finding "High Leverage" bugs.
* **Cost:** Pays $\mathcal{S}$ based on **Test Complexity**.
* **Reward:** Refund + 20 $\mathcal{S}$ Bounty if bug found.

### 🔵 Blue Team (The Defense)
* **Goal:** Survival.
* **Cost:** Pays $\mathcal{S}$ based on **Added Complexity** of the fix.
* **Revenue Streams:**
    1.  **The Grant:** Receives the complexity value of the test that broke the code.
    2.  **Refactoring Bonus:** Earns 2 $\mathcal{S}$ per complexity point removed.

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
* **TURNOVER.** Roles are swapped. The Attacker becomes the Defender (keeping their debt).

### Defensive Collapse (Defender Fails)
If the **Defender** runs out of tokens:
* **INSOLVENCY.** The Defense must delete code to survive (Refactor Only).

## 🚀 Quick Start

### 1. Install

[Install npm](https://nodejs.org/en/download/)

Next install the gemini-cli package,

    npm install -g @google/gemini-cli

Then run the command-line interface, `gemini` on its own to login.

Navigate to this directory and run:

```bash
pip3 install pytest ruff
gemini extensions install .
gemini
```

This will start the gemini cli interface.  To test the new /harden command, try:

    /harden buggy.py

### 2. Note of caution

A game should be played on a new feature branch.
