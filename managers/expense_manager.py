from models.expense import Expense


class ExpenseManager:

    def __init__(self):

        self.expenses = []

    def add_expense(self,amount,category,description,date):

        expense = Expense(amount,category,description,date)

        self.expenses.append(expense)

        print(
            "\nExpense Added Successfully."
        )

    def view_expenses(self):

        if len(self.expenses) == 0:

            print(
                "\nNo expenses available."
            )

            return

        print("\nAll Expenses")

        print("=" * 40)

        for expense in self.expenses:

            expense.display()