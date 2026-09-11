def generate_activity_id(activities):
    """Generate the next activity ID safely, such as A001, A002, A003."""

    # This function creates automatic activity IDs for new records.
    # We use IDs because update, delete, search, and archive features need a
    # clear way to identify one specific activity.
    # It checks the highest existing ID so deleted or archived records do not
    # cause duplicate IDs.
    highest_number = 0

    for activity in activities:
        activity_id = activity.get("activity_id", "")

        if activity_id.startswith("A"):
            try:
                number = int(activity_id[1:])

                if number > highest_number:
                    highest_number = number

            except ValueError:
                # If an activity has an unusual ID, we skip it instead of crashing.
                # This supports defensive coding.
                continue

    return "A" + str(highest_number + 1).zfill(3)


def find_activity_by_id(activities, activity_id):
    """Find one activity record using its activity ID."""

    # Each outreach activity should have a unique activity_id.
    # This loop checks every saved activity until it finds the matching ID.
    # lower() makes the search flexible, so A001 and a001 both work.
    for activity in activities:
        if activity.get("activity_id", "").lower() == activity_id.lower():
            return activity

    # If no matching activity is found, return None.
    # The menu can use this to show a clear "not found" message.
    return None


def search_activities(activities, field, search_value):
    """Search activities using a selected field and search value."""

    results = []

    # Convert the search value to lowercase so the search is not case-sensitive.
    # This means "health" and "Health" can still match.
    search_value = search_value.lower()

    # Check each activity and compare the chosen field with the search value.
    for activity in activities:
        field_value = str(activity.get(field, "")).lower()

        # If the search text appears inside the field value, save it as a result.
        if search_value in field_value:
            results.append(activity)

    return results


def calculate_total_hours(activities):
    """Calculate the total volunteer hours from all activities."""

    total = 0

    # Add the hours_contributed value from each activity.
    # float() is used because hours may include decimals, such as 2.5 hours.
    for activity in activities:
        total += float(activity.get("hours_contributed", 0))

    return total


def calculate_total_people_reached(activities):
    """Calculate the total number of people reached by all activities."""

    total = 0

    # people_reached shows community impact.
    # Adding all values gives a clear total impact figure for the report.
    for activity in activities:
        total += int(activity.get("people_reached", 0))

    return total


def count_activities_by_theme(activities):
    """Count how many activities belong to each GCGO theme."""

    theme_counts = {}

    # This dictionary groups activities by their GCGO theme.
    # Example result: {"Education": 3, "Health": 2}
    for activity in activities:
        theme = activity.get("gcgo_theme", "Unknown")

        if theme in theme_counts:
            theme_counts[theme] += 1
        else:
            theme_counts[theme] = 1

    return theme_counts


def count_activities_by_status(activities):
    """Count how many activities are planned, completed, cancelled, or archived."""

    status_counts = {}

    # Counting by status helps users understand project progress.
    # Example result: {"planned": 4, "completed": 6, "cancelled": 1, "archived": 2}
    for activity in activities:
        status = activity.get("status", "Unknown")

        if status in status_counts:
            status_counts[status] += 1
        else:
            status_counts[status] = 1

    return status_counts


def calculate_hours_by_theme(activities):
    """Calculate total volunteer hours for each GCGO theme."""

    hours_by_theme = {}

    # This report shows which GCGO themes received the most volunteer time.
    for activity in activities:
        theme = activity.get("gcgo_theme", "Unknown")
        hours = float(activity.get("hours_contributed", 0))

        if theme in hours_by_theme:
            hours_by_theme[theme] += hours
        else:
            hours_by_theme[theme] = hours

    return hours_by_theme


def calculate_people_by_theme(activities):
    """Calculate total people reached for each GCGO theme."""

    people_by_theme = {}

    # This report connects the application to community impact.
    # It shows how many people were reached under each GCGO theme.
    for activity in activities:
        theme = activity.get("gcgo_theme", "Unknown")
        people = int(activity.get("people_reached", 0))

        if theme in people_by_theme:
            people_by_theme[theme] += people
        else:
            people_by_theme[theme] = people

    return people_by_theme


def find_top_volunteer(activities):
    """Find the volunteer with the highest total contributed hours."""

    volunteer_hours = {}

    # This report adds the hours for each volunteer across all activities.
    # It helps identify the volunteer who contributed the most time.
    for activity in activities:
        volunteer = activity.get("volunteer_name", "Unknown")
        hours = float(activity.get("hours_contributed", 0))

        if volunteer in volunteer_hours:
            volunteer_hours[volunteer] += hours
        else:
            volunteer_hours[volunteer] = hours

    # If there are no activities, return None and 0 so the menu can print
    # a friendly message instead of crashing.
    if len(volunteer_hours) == 0:
        return None, 0

    top_volunteer = max(volunteer_hours, key=volunteer_hours.get)
    return top_volunteer, volunteer_hours[top_volunteer]


def build_report_text(activities):
    """Build a full outreach report that can be displayed or exported."""

    # This creates one complete report using the analysis functions above.
    # The same report can be printed in the terminal or saved as a text file.
    report = "QUERYMASTERS COMMUNITY OUTREACH REPORT\n"
    report += "=====================================\n\n"

    report += "Total activities: " + str(len(activities)) + "\n"
    report += "Total volunteer hours: " + str(calculate_total_hours(activities)) + "\n"
    report += "Total people reached: " + str(calculate_total_people_reached(activities)) + "\n\n"

    top_volunteer, hours = find_top_volunteer(activities)

    if top_volunteer is not None:
        report += "Top volunteer: " + top_volunteer + " with " + str(hours) + " hours\n\n"
    else:
        report += "Top volunteer: No volunteer data available\n\n"

    report += "Activities by GCGO theme:\n"
    for theme, count in count_activities_by_theme(activities).items():
        report += "- " + theme + ": " + str(count) + "\n"

    report += "\nActivities by status:\n"
    for status, count in count_activities_by_status(activities).items():
        report += "- " + status + ": " + str(count) + "\n"

    report += "\nVolunteer hours by GCGO theme:\n"
    for theme, hours in calculate_hours_by_theme(activities).items():
        report += "- " + theme + ": " + str(hours) + "\n"

    report += "\nPeople reached by GCGO theme:\n"
    for theme, people in calculate_people_by_theme(activities).items():
        report += "- " + theme + ": " + str(people) + "\n"

    return report