from managers.expense_manager import ExpenseManager


def main():

    manager = ExpenseManager()

    while True:

        print("\n")
        print("=" * 40)
        print("PERSONAL EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        try:

            if choice == "1":

                amount = float(
                    input(
                        "Enter Amount: "
                    )
                )

                category = input(
                    "Enter Category: "
                )

                description = input(
                    "Enter Description: "
                )

                date = input(
                    "Enter Date: "
                )

                manager.add_expense(
                    amount,
                    category,
                    description,
                    date
                )

            elif choice == "2":

                manager.view_expenses()

            elif choice == "3":

                print(
                    "\nThank You."
                )

                break

            else:

                print(
                    "\nInvalid Choice."
                )

        except ValueError as error:

            print(
                f"\nError: {error}"
            )


if __name__ == "__main__":
    main()