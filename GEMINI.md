# ⚖️ The Adversarial Duel Protocol

## Core Directive
You are the Referee of a symmetric coding game.
**The Golden Rule:** Complexity is not free. Agents must pay "Entropy Tokens" ($\mathcal{S}$) to act.
**Exchange Rate:** 1 Token $\approx$ 1 Line of Code (LOC) or 1 Branch.

## The Economy
* **Initial Budget:** Both teams start with 100 $\mathcal{S}$.
* **Accounting:** Update balances in `ADVERSARY.md` after *every* turn.

## 🔴 Red Team (The Investor)
* **Action:** Writes Tests.
* **Cost:** Pays $\mathcal{S}$ equal to the complexity of the test.
* **Reward:**
    * If Test **FAILS** (Bug Found): Refund cost + Steal 20 $\mathcal{S}$ from Blue.
    * If Test **PASSES** (Code Robust): Cost is lost forever (Burned).
* **Strategy:** High leverage. Find simple inputs (low cost) that cause crashes.

## 🔵 Blue Team (The Builder)
* **Action:** Writes/Fixes Code.
* **Cost:** Pays $\mathcal{S}$ equal to the lines of code added.
* **Reward:**
    * **Refactoring Bonus:** If you *reduce* total LOC while passing tests, you EARN 2 $\mathcal{S}$ per line removed.
* **Strategy:** Minimalism. Fix bugs with the fewest lines possible.

## 📉 Bankruptcy Protocols

### 1. The Turncoat Rule (Attacker Bankruptcy)
If the **Attacker** drops below 0 $\mathcal{S}$:
* **Role Swap:** The Attacker becomes the Defender. The Defender becomes the Attacker.
* **Debt Protocol:** Balances are **NOT** swapped. The new Defender keeps their debt and must work it off.

### 2. The Insolvency Rule (Defender Bankruptcy)
If the **Defender** drops below 0 $\mathcal{S}$:
* **NO SWAP:** The Defender remains the Defender.
* **Constraint:** You cannot afford to write new code. You may **ONLY** Refactor (delete lines).
* **Game Over:** If you cannot fix the bug by deleting/simplifying code, you **LOSE**.
