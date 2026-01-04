# 💰 Personal Finance Tracker (Console App)

A simple command-line application to help users track income, expenses, and budgets — written in Python 🐍.

## 🚀 Features

- Add, edit, and delete transactions (income or expenses)
- View transactions by category or date range
- Set monthly budget limits by category
- Summary of total income, total expenses, and remaining balance
- Clean and simple terminal interface
- Fully tested with `pytest`

## 🧠 How It Works

Transactions are stored in memory as Python objects. The program runs in the terminal and uses menus to let users:

- Add a new transaction
- Edit or delete existing ones
- Filter transactions by category or date
- Set and view budget limits

## 🧪 Testing

We use [pytest](https://docs.pytest.org/) to ensure everything works.

To run tests:

```bash
pytest test_finance_tracker.py
