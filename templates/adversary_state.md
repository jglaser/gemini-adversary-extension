# ⚔️ Adversarial Hardening: Round {{round}}

**Status:** {{status}}  *(Select one: RED_TURN, ARBITER_TURN, BLUE_TURN, EQUILIBRIUM)*
**Target File:** `{{target_file}}`

## 🔴 Red Team (Saboteur)
**Goal:** Create a test case that fails against current code.
- [ ] Test Created: `{{test_file}}`
- [ ] Test Execution Result: {{test_result}}

## ⚖️ Arbiter (Judge)
**Verdict:** {{verdict}} *(FAIR / UNFAIR)*
**Reasoning:**
> {{reasoning}}

## 🔵 Blue Team (Engineer)
**Goal:** Fix code to pass test without regression.
- [ ] Fix Applied
- [ ] Regression Tests Passed

---
*Instructions for Agent: Update this file after every action. Do not proceed to Blue Team if Arbiter says UNFAIR.*
