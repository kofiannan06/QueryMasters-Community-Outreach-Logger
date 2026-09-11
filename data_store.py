import json
import os

# The json file stores all outreach activity records.
# This is the path where all outreach activity records will be stored.
# We use a JSON file because the assignment requires file-based storage
# instead of a database.
DATA_FILE = "data/activities.json"

# This is the path where the exported report will be saved.
# We use a text file for the report because it is simple to open and read.
# This gives our project an extra file-handling feature beyond saving JSON data.
REPORT_FILE = "data/outreach_report.txt"


def load_activities():
    """We define a reusable block of code named load_activities to load outreach activities from the JSON file."""

    try:
        # Exception handling in Python.
        # If the data file does not exist yet, return an empty list.
        # This prevents the program from crashing the first time it runs.
        if not os.path.exists(DATA_FILE):
            return []

        # Open the JSON file in read mode and convert the stored JSON data
        # back into a Python list of dictionaries.
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        # If the JSON file is damaged or contains invalid JSON,
        # the program starts with an empty list instead of crashing.
        print("Warning: Data file is broken. Starting with an empty activity list.")
        return []

    except OSError:
        # OSError handles file problems such as permission issues
        # or unreadable files.
        print("Warning: Could not read the data file. Starting with an empty activity list.")
        return []


def save_activities(activities):
    """Save outreach activities to the JSON file."""

    try:
        # Create the data folder if it does not already exist.
        # This makes sure the program has a place to save the JSON file.
        os.makedirs("data", exist_ok=True)

        # Open the JSON file in write mode and save the activities list.
        # indent=4 makes the JSON file easier for humans to read.
        with open(DATA_FILE, "w") as file:
            json.dump(activities, file, indent=4)

        # Return True so the main program can know the save was successful.
        return True

    except OSError:
        # If saving fails, show an error message and return False.
        # This prevents the program from crashing unexpectedly.
        print("Error: Could not save activities.")
        return False


def export_report(report_text):
    """Save the generated outreach summary report to a text file."""

    try:
        # Create the data folder if it does not already exist.
        # This makes sure the program has a place to save the report file.
        os.makedirs("data", exist_ok=True)

        # Open the report file in write mode and save the report text.
        # We chose a .txt file because it is easy for users and lecturers to read.
        with open(REPORT_FILE, "w") as file:
            file.write(report_text)

        # Return True so the main program can confirm that the report was exported.
        return True

    except OSError:
        # If exporting fails, show an error message and return False.
        # This is defensive coding because the program handles the problem safely.
        print("Error: Could not export the report.")
        return False