# Gemini Code Duel (v2.1)

Turn code hardening into a balanced, zero-sum strategy game.

Unlike standard "Red Team" tools that spam infinite test cases, **The Duel** enforces a **Conservation of Complexity**. It pits two agents—an Attacker and a Defender—against each other in a game where "Entropy Tokens" ($\mathcal{S}$) measure the complexity of the system.

## 🏈 The Core Mechanic
**Complexity is not free.**
* **The Field:** The Codebase.
* **The Currency:** 1 Token ($\mathcal{S}$) $\approx$ 1 Line of Code (LOC) or Branch.
* **Starting Score:** Both teams start with **100 $\mathcal{S}$**.

### 🔴 Red Team (The Offense)
* **Goal:** Score points by finding "High Leverage" bugs (simple inputs -> expensive crashes).
* **Cost:** Pays $\mathcal{S}$ to execute plays (write tests).
* **Risk:** If the test PASSES (Defense holds), the tokens are burned (Down lost).
* **Reward:** If the test FAILS (Touchdown), Red gets a refund + steals **20 $\mathcal{S}$** from Blue.

### 🔵 Blue Team (The Defense)
* **Goal:** Hold the line (Survival & Minimalism).
* **Cost:** Pays $\mathcal{S}$ to plug holes (write fixes).
* **Reward:** **Refactoring Bonus.** If you simplify the architecture (delete lines) while maintaining pass rates, you **EARN 2 $\mathcal{S}$** per line removed.

---

## 📉 Game Rules

### 1. The Turnover Rule (Attacker Fails)
If the **Attacker** runs out of tokens (fails to find bugs):
* **TURNOVER.** Roles are swapped immediately.
* **The Penalty:** The former Attacker becomes the Defender. They keep their token deficit (Debt) and must Refactor code to get back in the game.

### 2. Defensive Collapse (Defender Fails)
If the **Defender** runs out of tokens (writes spaghetti code to fix bugs):
* **NO SWAP.** The Defense has collapsed.
* **Constraint:** The Defender enters **Desperation Mode**. They cannot write *new* lines of code. They can only fix bugs by deleting/simplifying existing code.

### 💀 Game Over
If the Defender is in Desperation Mode and cannot fix the bug without adding complexity:
1.  **Defeat.** The architecture is too brittle to support the requirements.
2.  **The Fix:** Perform a **Hard Reset**.
    * Delete `ADVERSARY.md`.
    * Run `/harden` to kickoff a new game.

---

## 🚀 Quick Start

### 1. Install
Navigate to this directory and run:

```bash
gemini extensions install .
