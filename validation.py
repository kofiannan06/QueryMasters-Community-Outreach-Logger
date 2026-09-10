from datetime import datetime

# These are the only status values accepted by the outreach activity system.
# Keeping them in one list makes validation consistent across the application.
# It also prevents incorrect status values from being saved into the data file.
# We added "archived" because one of our extra features is safer deletion:
# instead of permanently removing an activity, we can mark it as archived.
VALID_STATUSES = ["planned", "completed", "cancelled", "archived"]


def is_not_empty(value):
    """Check that a required text field contains real text."""

    # Required fields such as activity name, location, GCGO theme, and volunteer
    # name should not be blank. strip() removes spaces before checking, so an
    # input like "   " is treated as empty.
    return value.strip() != ""


def is_valid_date(date_text):
    """Check that a date follows the required YYYY-MM-DD format."""

    try:
        # datetime.strptime attempts to convert the text into a real date.
        # We use YYYY-MM-DD because it is clear, consistent, and easy to compare.
        datetime.strptime(date_text, "%Y-%m-%d")
        return True

    except ValueError:
        # ValueError happens when the text is not a valid date, such as
        # "2026-15-40" or "next Monday". Returning False lets the menu ask
        # the user to enter the date again instead of crashing.
        return False


def is_positive_number(value):
    """Check that a value can be converted into a number greater than zero."""

    try:
        # Volunteer hours must be greater than zero because completed work
        # should record an actual amount of time. float() allows decimal hours
        # such as 1.5 or 2.75.
        number = float(value)
        return number > 0

    except ValueError:
        # ValueError happens when the user enters text instead of a number.
        # Returning False supports defensive coding and prevents a program crash.
        return False


def is_zero_or_positive_integer(value):
    """Check that a value can be converted into a whole number of zero or more."""

    try:
        # People reached must be a whole number because we are counting people.
        # Zero is allowed for planned activities that have not happened yet.
        number = int(value)
        return number >= 0

    except ValueError:
        # If the input cannot be converted into an integer, the function returns
        # False so the program can request a valid number from the user.
        return False


def is_valid_status(status):
    """Check that the activity status is one of the accepted status values."""

    # lower() allows users to type values like "Planned" or "COMPLETED" while
    # still comparing them with the accepted lowercase status list.
    return status.lower() in VALID_STATUSES