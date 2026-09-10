# Community Outreach Activity Logger

## 1. Problem Statement

Community outreach activities usually involve important information that must be recorded for reference, reporting, and future planning. These activities may involve multiple volunteers, different locations, activity dates, GCGO themes, hours contributed, people reached, and activity statuses.

Without a well-organised system, it can become difficult to track volunteer participation, monitor outreach progress, update activity records, and understand the overall impact of outreach efforts. Manual records can also lead to missing information, repeated entries, and difficulty generating accurate summaries.

The QueryMasters Community Outreach Activity Logger aims to provide a simple Python command-line system for recording, managing, searching, and analysing outreach activity data. The application uses a menu-driven interface and stores records in a JSON file so that data can be saved and reloaded after the program closes.

## 2. Functional Requirements

The application should allow users to:

1. Add a new outreach activity.
2. View all recorded outreach activities.
3. Update an existing outreach activity using its activity ID.
4. Delete or archive an outreach activity.
5. Confirm before deleting a record to avoid accidental data loss.
6. Search and filter outreach activities by volunteer name, GCGO theme, location, status, or date.
7. Automatically generate unique activity IDs such as A001, A002, and A003.
8. Save activity records to a JSON file.
9. Load previously saved records when the application starts.
10. Validate user input before storing records.
11. Handle invalid input and file errors without crashing.
12. Generate total volunteer hours.
13. Generate activities grouped by GCGO theme.
14. Generate activities grouped by status.
15. Generate total people reached.
16. Generate people reached by GCGO theme.
17. Identify the top volunteer by total hours contributed.
18. Export a full outreach report to a text file.

## 3. Data Fields

Each outreach activity will be represented as a Python dictionary and stored inside a list. The list of records will be saved in data/activities.json.

| Field | Purpose |
|---|---|
| activity_id | Unique identifier for the activity, generated automatically by the system. |
| activity_name | Name or title of the outreach activity. |
| gcgo_theme | GCGO theme associated with the activity, such as education, health, sustainability, or community development. |
| location | Location where the activity takes place. |
| date | Date on which the activity occurs, written in YYYY-MM-DD format. |
| volunteer_name | Name of the volunteer linked to the activity record. |
| hours_contributed | Number of hours contributed by the volunteer. |
| people_reached | Number of people reached through the outreach activity. |
| status | Current activity status: planned, completed, cancelled, or archived. |
| notes | Additional information about the activity. |

## 4. Validation Requirements

The application should validate the following inputs before storing records:

| Input | Validation Rule |
|---|---|
| Activity name | Must not be empty. |
| GCGO theme | Must not be empty. |
| Location | Must not be empty. |
| Date | Must follow the YYYY-MM-DD format. |
| Volunteer name | Must not be empty. |
| Hours contributed | Must be a positive number greater than 0. |
| People reached | Must be 0 or a positive whole number. |
| Status | Must be one of: planned, completed, cancelled, or archived. |

The system should use validation and try/except error handling to prevent crashes when users enter incorrect values or when file problems occur.

## 5. File Storage Requirements

The application will use file-based storage instead of a database, as required by the assessment.

The main data file will be:

```text
data/activities.json

## 6. Analysis and Reporting Requirements
The application should include more than two reporting features to provide useful outreach insights.
Required reports include:

1. Total volunteer hours.
2. Activities grouped by GCGO theme.
3. Activities grouped by status.
4. Total people reached.
5. People reached by GCGO theme.
6. Top volunteer by total hours contributed.
7. Exported full summary report.
These reports help users understand volunteer effort, activity progress, and community impact.

7. GCGO Link
This project connects to Global Challenges and Global Opportunities because community outreach activities often support social impact goals such as education, health, sustainability, and community development.
For example:
- Education outreach activities can support learning access and digital skills.
- Health outreach activities can support awareness and community well-being.
- Sustainability activities can support environmental responsibility.
- Community development activities can support local improvement and inclusion.
By tracking activities, volunteer hours, and people reached, the system helps users understand how outreach work contributes to positive community impact.


8. Proposed File Structure
QueryMasters-Community-Outreach-Logger/
│
├── main.py
├── data_store.py
├── validation.py
├── processing.py
├── README.md
├── requirements_note.md
├── sources_ai_disclosure.md
│
└── data/
    ├── activities.json
    └── outreach_report.txt

9. Success Criteria
The project will be successful if:
1. The application runs in the terminal using python main.py.
2. The menu remains active until the user chooses to exit.
3. Users can add, view, update, delete, archive, search, and filter activity records.
4. Activity records are saved and reloaded using JSON file storage.
5. Invalid menu choices and invalid input are handled safely.
6. At least two analysis/reporting features work correctly.
7. Additional reports provide useful summaries of outreach impact.
8. The report export feature creates a readable text file.
9. The code is separated into clear modules and functions.
10. The team can explain the code and features during the demonstration.


10. Scope
This project will use:
- Python 3 standard library
- Variables
- if, elif, and else
- for and while loops
- Functions
- Lists
- Dictionaries
- Searching and filtering
- Basic calculations
- Input validation
- try/except
- JSON file handling
- Multiple Python files/modules
This project will not use:
- Databases
- Web applications
- Graphical user interfaces
- External Python packages
- Object-oriented class design


11. Module Responsibilities
File    Responsibility
main.py Runs the command-line menu and connects user choices to the correct functions.
data_store.py   Loads activities, saves activities, and exports reports using files.
validation.py   Checks user input before records are saved.
processing.py   Handles searching, filtering, calculations, reports, and activity ID generation.
data/activities.json    Stores outreach activity records.
data/outreach_report.txt    Stores the exported report summary.
