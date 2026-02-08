# Gemini Adversarial Duel (v2.1)

Turn code hardening into a balanced, resource-constrained strategy game.

## ⚖️ The Core Mechanic
**Complexity is not free.**
* **Exchange Rate:** 1 Token ($\mathcal{S}$) $\approx$ 1 Line of Code (LOC) or Branch.
* **Starting Budget:** Both teams start with **100 $\mathcal{S}$**.

### 📉 Bankruptcy Rules

#### 1. The Turncoat Rule (Attacker Fails)
If the **Attacker** goes bankrupt (spends tokens on failed tests):
* **ROLES SWAP.** The Attacker is demoted to Defender and must refactor to pay off their debt.

#### 2. The Insolvency Rule (Defender Fails)
If the **Defender** goes bankrupt (spends too much on complex fixes):
* **NO SWAP.**
* The Defender enters **Insolvency Mode**.
* They **cannot** write new lines of code. They can **only** fix bugs by deleting code (Refactoring).
* If they cannot fix the bug by simplifying, they lose the game.

## 🚀 Quick Start

### 1. Install
Navigate to this directory and run:

```bash
gemini extensions install .
