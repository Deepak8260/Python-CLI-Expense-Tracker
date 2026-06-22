from models.expense import Expense

from storage.file_handler import FileHandler


class ExpenseManager:

    def __init__(self):

        self.expenses = (
            FileHandler.load_expenses()
        )

    def add_expense(
        self,
        amount,
        category,
        description,
        date
    ):

        expense = Expense(
            amount,
            category,
            description,
            date
        )

        self.expenses.append(
            expense
        )

        FileHandler.save_expenses(
            self.expenses
        )

        print(
            "\nExpense Added Successfully."
        )

    def view_expenses(
        self
    ):

        if len(
            self.expenses
        ) == 0:

            print(
                "\nNo expenses available."
            )

            return

        print("\nAll Expenses")
        print("=" * 40)

        for index, expense in enumerate(
            self.expenses,
            start=1
        ):

            print(
                f"\nExpense ID: {index}"
            )

            expense.display()

    def search_expense(
        self,
        category
    ):

        found = False

        for expense in self.expenses:

            if (
                expense.category.lower()
                ==
                category.lower()
            ):

                expense.display()

                found = True

        if not found:

            print(
                "\nNo matching expenses found."
            )

    def update_expense(
        self,
        expense_id,
        amount,
        category,
        description,
        date
    ):

        try:

            expense = (
                self.expenses[
                    expense_id - 1
                ]
            )

            expense.amount = amount
            expense.category = category
            expense.description = description
            expense.date = date

            FileHandler.save_expenses(
                self.expenses
            )

            print(
                "\nExpense Updated Successfully."
            )

        except IndexError:

            print(
                "\nInvalid Expense ID."
            )

    def delete_expense(
        self,
        expense_id
    ):

        try:

            self.expenses.pop(
                expense_id - 1
            )

            FileHandler.save_expenses(
                self.expenses
            )

            print(
                "\nExpense Deleted Successfully."
            )

        except IndexError:

            print(
                "\nInvalid Expense ID."
            )