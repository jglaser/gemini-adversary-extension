# Gemini Code Duel (v2.8): The Satellite Edition 🛰️

Turn code hardening into a balanced, zero-sum strategy game.

## 🛰️ Satellite Recon (MCP)
To prevent "Delay of Game" caused by the Agent looping through file directories, we have added a **Repo Reader Tool**.
* **The Tool:** `tools/repo_reader.py`
* **The Function:** Scans the entire project (ignoring `.git`) and dumps it as XML.
* **The Benefit:** The Agent gets "God View" of the code in 1 turn, instead of 10 turns of `ls -R`.

## 🧱 The Immutable Source Rule
**Production Code is Read-Only for the Red Team.**
* **The Offense:** Sabotage (Red Team modifies source code to cause a failure).
* **The Fine:** **100 $\mathcal{S}$ (Immediate Forfeiture).**

## ⏱️ Delay of Game
**Time is money.**
* **The Offense:** Stalling (Infinite loops, timeouts).
* **The Fine:** **5 $\mathcal{S}$**.

## ⚖️ The Economy
* **Currency:** 1 Token ($\mathcal{S}$) = 1 Cyclomatic Complexity Point (C901).
* **Subsidy:** When Red finds a bug, the Complexity of the test is transferred to Blue.

### 🔴 Red Team (The Offense)
* **Goal:** Score touchdowns by finding bugs.
* **Revenue:** Bounties (20 $\mathcal{S}$) + Restitution Payments (50 $\mathcal{S}$).

### 🔵 Blue Team (The Defense)
* **Goal:** Survival.
* **Revenue:** Subsidy (Grant) + Refactoring Bonus.

---

## 🚀 Quick Start
1. `pip3 install mcp`
2. `gemini extensions install .`
3. `/harden`

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
