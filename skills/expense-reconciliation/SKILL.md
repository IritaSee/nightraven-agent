---
name: expense-reconciliation
description: Calculate debt for shared expenses and update ledger.csv tracking.
---

# Expense Reconciliation

Use this skill to calculate debts or surpluses from shared expenses (e.g., trips, projects) and record the final balances in the user's finance tracker.

## When to Use
- After a shared trip or event where multiple people paid for different items.
- When the user needs to "equalize" or "settle up" with an associate.
- When updating `ledger.csv` with new debt/credit entries.

## Steps

1.  **Gather Data**:
    - List all expenses incurred during the event.
    - Identify who paid for each item.
    - Identify the total number of participants sharing the cost.
2.  **Calculate Totals**:
    - Sum the total cost of the event.
    - Calculate the "fair share" per person (Total / Number of Participants).
3.  **Determine Balances**:
    - For each person: `Balance = Amount Paid - Fair Share`.
    - Positive balance means they are owed money; negative means they owe money.
4.  **Update Ledger**:
    - Read the current `ledger.csv` (usually in `finance/ledger.csv`).
    - Append a new row for the reconciliation.
    - Format: `Date, Category, Description, Amount, Person, Status`.
5.  **Confirm with User**:
    - Present the breakdown and the final amount to be paid/received.

## Tools Used
- `read_file`: To read `ledger.csv`.
- `edit_file` or `write_file`: To update the ledger.
- `excel-editor`: If the ledger is in `.xlsx` format.

## Example

**Scenario**: Jakarta Trip with Angel.
- User paid: Rp 2,000,000 (Hotel)
- Angel paid: Rp 2,450,000 (Car Repair + Food)
- Total: Rp 4,450,000
- Fair Share (2 people): Rp 2,225,000
- User Balance: 2,000,000 - 2,225,000 = -Rp 225,000 (User owes Angel)

**Ledger Entry**:
`2026-05-27, Travel, Jakarta Trip Reconciliation, -225000, Angel, Pending`

## Output Format
- A clear breakdown of expenses.
- The final calculation showing who owes whom.
- Confirmation that the ledger has been updated.
