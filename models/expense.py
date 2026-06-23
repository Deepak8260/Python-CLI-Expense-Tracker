from utils.validators import Validators


class Expense:

    def __init__(
        self,
        amount,
        category,
        description,
        date
    ):

        self.amount = (
            Validators.validate_amount(
                amount
            )
        )

        self.category = (
            Validators.validate_category(
                category
            )
        )

        self.description = (
            Validators.validate_description(
                description
            )
        )

        self.date = (
            Validators.validate_date(
                date
            )
        )

    def display(self):

        print("\nExpense Details")
        print("-" * 30)

        print(f"Amount      : {self.amount}")
        print(f"Category    : {self.category}")
        print(f"Description : {self.description}")
        print(f"Date        : {self.date}")