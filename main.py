from managers.expense_manager import (
    ExpenseManager
)


def main():

    manager = ExpenseManager()

    while True:

        print("\n")
        print("=" * 40)
        print(
            "PERSONAL EXPENSE TRACKER"
        )
        print("=" * 40)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Exit")

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
                    "Enter Date (YYYY-MM-DD): "
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

                category = input(
                    "Enter Category: "
                )

                manager.search_expense(
                    category
                )

            elif choice == "4":

                expense_id = int(
                    input(
                        "Enter Expense ID: "
                    )
                )

                amount = float(
                    input(
                        "Enter New Amount: "
                    )
                )

                category = input(
                    "Enter New Category: "
                )

                description = input(
                    "Enter New Description: "
                )

                date = input(
                    "Enter New Date: "
                )

                manager.update_expense(
                    expense_id,
                    amount,
                    category,
                    description,
                    date
                )

            elif choice == "5":

                expense_id = int(
                    input(
                        "Enter Expense ID: "
                    )
                )

                manager.delete_expense(
                    expense_id
                )

            elif choice == "6":

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