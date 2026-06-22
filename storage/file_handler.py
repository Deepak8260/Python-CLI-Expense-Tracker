import json

from models.expense import Expense


class FileHandler:

    FILE_PATH = "data/expenses.json"

    @classmethod
    def save_expenses(
        cls,
        expenses
    ):

        data = []

        for expense in expenses:

            data.append(
                {
                    "amount": expense.amount,
                    "category": expense.category,
                    "description": expense.description,
                    "date": expense.date
                }
            )

        with open(
            cls.FILE_PATH,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @classmethod
    def load_expenses(
        cls
    ):

        try:

            with open(
                cls.FILE_PATH,
                "r"
            ) as file:

                data = json.load(
                    file
                )

            expenses = []

            for item in data:

                expense = Expense(
                    item["amount"],
                    item["category"],
                    item["description"],
                    item["date"]
                )

                expenses.append(
                    expense
                )

            return expenses

        except FileNotFoundError:

            return []

        except json.JSONDecodeError:

            return []