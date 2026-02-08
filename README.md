# Gemini Adversarial Duel (v2.1)

Turn code hardening into a balanced, resource-constrained strategy game.

Unlike standard "Red Team vs. Blue Team" loops where the attacker has infinite resources to generate complex tests, **The Duel** enforces a **Conservation of Complexity**. Agents must pay "Entropy Tokens" ($\mathcal{S}$) to write code or tests.

## ⚖️ The Core Mechanic
**Complexity is not free.**
* **Exchange Rate:** 1 Token ($\mathcal{S}$) $\approx$ 1 Line of Code (LOC) or Branch.
* **Starting Budget:** Both teams start with **100 $\mathcal{S}$**.

### 🔴 Red Team (The Investor)
* **Goal:** Find "High Leverage" bugs (simple inputs that cause expensive crashes).
* **Cost:** Pays $\mathcal{S}$ to write tests.
* **Risk:** If the test PASSES (no bug found), the tokens are burned.
* **Reward:** If the test FAILS (bug found), Red gets a refund + steals **20 $\mathcal{S}$** from Blue.

### 🔵 Blue Team (The Builder)
* **Goal:** Survival & Minimalism.
* **Cost:** Pays $\mathcal{S}$ to write fixes.
* **Reward:** **Refactoring Bonus.** If you *reduce* total LOC while passing tests, you **EARN 2 $\mathcal{S}$** per line deleted.

---

## 📉 Bankruptcy Rules

### 1. The Turncoat Rule (Attacker Fails)
If the **Attacker** goes bankrupt (spends tokens on failed tests):
* **ROLES SWAP.** The Attacker is demoted to Defender.
* **Debt Protocol:** They keep their negative balance (Debt) and must Refactor code to earn tokens back.

### 2. The Insolvency Rule (Defender Fails)
If the **Defender** goes bankrupt (spends too much on complex fixes):
* **NO SWAP.**
* The Defender enters **Insolvency Mode**.
* They **cannot** write new lines of code. They can **only** fix bugs by deleting code (Refactoring).

### 💀 Losing the Game
If the Defender cannot fix the bug via refactoring (Insolvency) and runs out of moves:
1.  **Game Over.** The architecture is too brittle.
2.  **The Fix:** Perform a **Hard Reset**.
    * Delete `ADVERSARY.md`.
    * Run `/harden` to restart with fresh budgets.

---

## 🚀 Quick Start

### 1. Install
Navigate to this directory and run:

```bash
gemini extensions install .
