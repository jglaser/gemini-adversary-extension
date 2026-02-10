# Gemini Code Duel (v2.3): The Ruff Referee

Turn code hardening into a balanced, zero-sum strategy game.

Unlike standard "Red Team" tools that spam infinite test cases, **The Duel** enforces a **Conservation of Complexity**. We use **Ruff** (The Referee) to penalize "Rough Play" (Code Golfing) and ensure fair accounting.

## 🦓 The Core Mechanic
**Complexity is not free.**
* **The Referee:** `ruff` (linter).
* **The Currency:** 1 Token ($\mathcal{S}$) = 1 Cyclomatic Complexity Point (C901).
* **Starting Score:** Both teams start with **100 $\mathcal{S}$**.

### 🔴 Red Team (The Offense)
* **Goal:** Score touchdowns by finding "High Leverage" bugs.
* **Cost:** Pays $\mathcal{S}$ based on **Test Complexity**.
* **Risk:** If the test PASSES (Defense holds), the tokens are burned.
* **Reward:** If the test FAILS (Bug Found), Red gets a refund + steals **20 $\mathcal{S}$** from Blue.

### 🔵 Blue Team (The Defense)
* **Goal:** Hold the line (Survival & Minimalism).
* **Cost:** Pays $\mathcal{S}$ based on **Added Complexity** to the codebase.
* **Reward:** **Refactoring Bonus.** If you simplify the architecture (reduce C901 score) while maintaining pass rates, you **EARN 2 $\mathcal{S}$** per point removed.

---

## 🚩 Penalties & Fouls

### Unnecessary Roughness (Code Golfing)
Merging 10 lines of logic into 1 dense line to "save money" is a foul.
* **The Call:** `ruff` counts branches, not lines. A dense one-liner still costs tokens.
* **The Fine:** If code is messy (`ruff format` fails), the Referee levies a **5 $\mathcal{S}$ Fine**.

### Turnover on Downs (Attacker Fails)
If the **Attacker** runs out of tokens:
* **TURNOVER.** Roles are swapped.
* **The Penalty:** The former Attacker becomes the Defender (keeping their debt) and must Refactor to get back in the game.

### Defensive Collapse (Defender Fails)
If the **Defender** runs out of tokens:
* **NO SWAP.** The Defense has collapsed.
* **Constraint:** The Defender enters **Insolvency Mode**. They cannot write *new* logic. They can only fix bugs by deleting/simplifying existing code.

---

## 🚀 Quick Start

### 1. Install
Navigate to this directory and run:

```bash
gemini extensions install .
