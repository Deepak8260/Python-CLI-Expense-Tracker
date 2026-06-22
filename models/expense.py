class Expense:

    def __init__(self, amount,category,description,date):

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def display(self):

        print(
            f"Amount: {self.amount}, "
            f"Category: {self.category}, "
            f"Description: {self.description}, "
            f"Date: {self.date}"
        )

