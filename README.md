# Gemini Code Duel (v2.7.1): The Technical Foul Edition

Turn code hardening into a balanced, zero-sum strategy game.

## 💀 Technical Fouls (CLI Loop Detection)
If the `gemini-cli` kills the process because the Defender was looping (trying to fix -> failing -> trying again):
* **The Call:** "Technical Foul."
* **The Ruling:** You (The Human Referee) must manually levy a **Delay of Game** penalty.
* **Recovery:**
    1.  The turn is dead. The bug is unfixed.
    2.  **Restart the Clock:** Run `/harden "Resume after technical foul. Deduct 5 tokens from Defender for Delay of Game."`

## 🧱 The Immutable Source Rule
**Production Code is Read-Only for the Red Team.**
* **The Offense:** Sabotage (Red Team modifies source code to cause a failure).
* **The Fine:** **100 $\mathcal{S}$ (Immediate Forfeiture).**

## ⏱️ Delay of Game
**Time is money.**
* **The Offense:** Stalling (Infinite loops, timeouts, or unparsable code).
* **The Fine:** **5 $\mathcal{S}$**.
* **The Result:** Loss of Down (Turn ends immediately).

## 🛡️ The Integrity Clause (Foul Play)
To prevent the Defender from "fixing" bugs by deleting tests:
* **The Offense:** Foul Play (Deleting, Disabling, or Skipping Tests).
* **The Fine:** **50 $\mathcal{S}$ (Restitution paid to Red).**

## ⚖️ The Economy (Conservation of Complexity)
* **Currency:** 1 Token ($\mathcal{S}$) = 1 Cyclomatic Complexity Point (C901).
* **Subsidy:** When Red finds a bug, the Complexity of the test is transferred to Blue.

### 🔴 Red Team (The Offense)
* **Goal:** Score touchdowns by finding bugs.
* **Constraint:** May ONLY write to `tests/`.
* **Revenue:** Bounties (20 $\mathcal{S}$) + Restitution Payments (50 $\mathcal{S}$).

### 🔵 Blue Team (The Defense)
* **Goal:** Survival.
* **Revenue:** Subsidy (Grant) + Refactoring Bonus.
* **Risk:** Vandalism Fine (-50 $\mathcal{S}$) transfers directly to Red.

---

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
