from datetime import datetime, timedelta

def calculate_due_date(created_date: str, terms: int) -> str:
    """Calculates the due date by adding a specified number of days to the created date.

    Args:
        created_date: The created date string in YYYY-MM-DD format.
        terms: The number of days to add to the created date.

    Returns:
        The due date string in YYYY-MM-DD format.

    Raises:
        ValueError: If the created date string is not in the expected format.
    """

    try:
        date_format = "%Y-%m-%d"
        datetime_obj = datetime.strptime(created_date, date_format)
    except ValueError:
        raise ValueError(f"Invalid created date format. Expected format: {date_format}")

    new_date = datetime_obj + timedelta(days=terms)
    due_date_str = new_date.strftime(date_format)
    return due_date_str