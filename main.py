from managers.expense_manager import ExpenseManager


def main():

    manager = ExpenseManager()

    try:

        manager.add_expense(250,"Food","Pizza","2026-06-22")

        manager.add_expense(150,"Travel","Auto","2026-06-22")

        manager.view_expenses()

    except ValueError as error:

        print(
            f"Error: {error}"
        )


if __name__ == "__main__":
    main()