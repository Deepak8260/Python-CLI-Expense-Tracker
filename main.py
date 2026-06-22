from models.expense import Expense


def main():

    expenses = []

    try:

        expense1 = Expense(250,"Food","Pizza","2026-06-22")

        expense2 = Expense(150,"Travel","Auto","2026-06-22")

        expenses.append(expense1)
        expenses.append(expense2)

        print("\nExpenses:\n")

        for expense in expenses:
            expense.display()

    except ValueError as error:

        print(
            f"Error: {error}"
        )


if __name__ == "__main__":
    main()