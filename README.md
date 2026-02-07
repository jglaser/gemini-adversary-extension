# Gemini Adversarial Duel (v2.0)

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
* **Reward:** **Refactoring Bonus.** If you reduce the total line count while passing tests, you **EARN 2 $\mathcal{S}$** per line deleted.

### 🔄 The Turncoat Rule
If the Red Team goes bankrupt (Balance < 0), **Roles are SWAPPED.**
* Red becomes the Builder (forced to refactor to earn back tokens).
* Blue becomes the Attacker.

---

## 🚀 Quick Start

### 1. Install
Navigate to this directory and run:

```bash
gemini extensions install .
