import pytest
from Finance import FinanceTracker  # Capital F matches your filename
from datetime import datetime


@pytest.fixture
def tracker():
    return FinanceTracker()

def test_add_transaction(tracker):
    tracker.add_transaction("Salary", 3000, "2025-03-01", "Income")
    assert len(tracker.transactions) == 1
    assert tracker.transactions[0].description == "Salary"
    assert tracker.transactions[0].amount == 3000
    assert tracker.transactions[0].category == "Income"

def test_edit_transaction(tracker):
    tracker.add_transaction("Old Salary", 1000, "2025-03-01", "Income")
    tracker.edit_transaction(0, "New Salary", 2000, "2025-03-02", "Income")
    assert tracker.transactions[0].description == "New Salary"
    assert tracker.transactions[0].amount == 2000
    assert tracker.transactions[0].date == datetime(2025, 3, 2)

def test_delete_transaction(tracker):
    tracker.add_transaction("Groceries", -50, "2025-03-01", "Food")
    tracker.delete_transaction(0)
    assert len(tracker.transactions) == 0

def test_budget_setting_and_summary(tracker, capsys):
    tracker.budget.set_budget("Food", 200)
    tracker.add_transaction("Groceries", -50, "2025-03-01", "Food")
    tracker.budget_summary()
    captured = capsys.readouterr()
    assert "Spent $50.00 / Limit $200.00" in captured.out

def test_list_transactions_with_filters(tracker, capsys):
    tracker.add_transaction("Rent", -1000, "2025-03-01", "Housing")
    tracker.add_transaction("Groceries", -100, "2025-03-10", "Food")
    tracker.list_transactions(category="Food")
    captured = capsys.readouterr()
    assert "Groceries" in captured.out
    assert "Rent" not in captured.out
def test_edit_nonexistent_transaction(tracker, capsys):
    tracker.edit_transaction(5, "Test", 100, "2025-03-01", "Misc")
    captured = capsys.readouterr()
    assert "Invalid transaction index." in captured.out

def test_set_zero_or_negative_budget(tracker):
    tracker.budget.set_budget("Food", 0)
    assert tracker.budget.get_budget("Food") == 0

    tracker.budget.set_budget("Entertainment", -50)
    assert tracker.budget.get_budget("Entertainment") == -50

def test_income_vs_expense_filtering(tracker, capsys):
    tracker.add_transaction("Salary", 3000, "2025-03-01", "Income")
    tracker.add_transaction("Rent", -1200, "2025-03-01", "Housing")
    tracker.list_transactions(category="Income")
    captured_income = capsys.readouterr()
    assert "Salary" in captured_income.out
    assert "Rent" not in captured_income.out

    tracker.list_transactions(category="Housing")
    captured_expense = capsys.readouterr()
    assert "Rent" in captured_expense.out
    assert "Salary" not in captured_expense.out

