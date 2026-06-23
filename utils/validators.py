from datetime import datetime


class Validators:

    @staticmethod
    def validate_amount(
        amount
    ):

        if amount <= 0:

            raise ValueError(
                "Amount must be greater than zero."
            )

        return amount

    @staticmethod
    def validate_category(
        category
    ):

        if not category.strip():

            raise ValueError(
                "Category cannot be empty."
            )

        return category

    @staticmethod
    def validate_description(
        description
    ):

        if not description.strip():

            raise ValueError(
                "Description cannot be empty."
            )

        return description

    @staticmethod
    def validate_date(
        date
    ):

        try:

            datetime.strptime(
                date,
                "%Y-%m-%d"
            )

            return date

        except ValueError:

            raise ValueError(
                "Date must be in YYYY-MM-DD format."
            )