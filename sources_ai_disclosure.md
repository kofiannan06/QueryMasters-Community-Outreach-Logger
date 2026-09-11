# Sources and AI Disclosure

## Project Information

**Project Name:** QueryMasters Community Outreach Logger  
**Project Type:** Python menu-driven command-line application  
**Scenario:** Community Outreach Activity Logger  
**Module:** Introduction to Programming and Databases  
**Team Name:** QueryMasters  

## Purpose of the Project

QueryMasters Community Outreach Logger is designed to record, manage, and analyse community outreach activities using a simple Python terminal-based system. The application tracks activity names, GCGO themes, locations, dates, volunteers, hours contributed, people reached, statuses, and notes.

The project supports basic outreach coordination by helping users store structured activity data, search records, update information, and generate reports such as total volunteer hours, activities by GCGO theme, activities by status, people reached, and top volunteer contribution.

## Technical Sources Used

This project uses only Python standard library features. No external Python packages or third-party code libraries were used.

The following Python modules were used:

- `json`: used to save and load outreach activity records in JSON format.
- `os`: used to check whether files and folders exist before reading or writing data.
- `datetime`: used to validate dates using the `YYYY-MM-DD` format.

Official documentation references:

- Python Software Foundation. (2026). *json — JSON encoder and decoder*. https://docs.python.org/3/library/json.html
- Python Software Foundation. (2026). *os — Miscellaneous operating system interfaces*. https://docs.python.org/3/library/os.html
- Python Software Foundation. (2026). *datetime — Basic date and time types*. https://docs.python.org/3/library/datetime.html

## Comparison With Existing Organisational Systems

Our project is a beginner-level academic prototype, but it is inspired by real organisational systems used for volunteer and nonprofit programme management.

Professional platforms such as Salesforce Nonprofit Cloud and Benevity provide advanced features for managing programmes, volunteers, services, attendance, reporting, and impact measurement. Salesforce describes programme management systems as tools that help organisations manage programmes, benefits, enrollments, participation, and stakeholder reporting. Benevity also provides volunteer management tools for time tracking, opportunity management, participation reporting, and impact summaries.

Our project follows the same basic idea on a smaller scale. Instead of using cloud dashboards, databases, automation, or enterprise integrations, QueryMasters Community Outreach Logger focuses on the foundational programming version of the same problem: storing outreach records, tracking volunteer hours, searching data, and producing simple reports.

### Comparison Table

| Area | Professional Systems | QueryMasters Project |
|---|---|---|
| Data storage | Cloud databases and enterprise platforms | JSON file storage |
| User interface | Web/mobile dashboards | Terminal menu interface |
| Volunteer tracking | Automated time tracking and dashboards | Manual entry of volunteer hours |
| Reporting | Advanced analytics and visual dashboards | Text-based reports and TXT export |
| Search/filter | Advanced filters and database queries | Simple Python search/filter functions |
| Scope | Large organisations and nonprofits | Small student outreach team |
| Technology level | Enterprise software | Python standard library |

This comparison shows that our project is realistic because it solves a real type of organisational problem, but it remains appropriate for the module level by using variables, functions, lists, dictionaries, loops, validation, exception handling, and file persistence.

## External References

Salesforce. (2026). *Program Management*. Salesforce Help. https://help.salesforce.com/s/articleView?id=ind.prog_case_mgmt_prog_mgmt.htm

Salesforce. (2026). *Program and Case Management*. Salesforce Help. https://help.salesforce.com/s/articleView?id=ind.prog_case_mgmt.htm

Benevity. (2026). *Volunteer Management Software*. https://benevity.com/products/volunteer

United Nations. (2026). *The Sustainable Development Goals*. https://www.un.org/sustainabledevelopment/sustainable-development-goals/

United Nations Department of Economic and Social Affairs. (2026). *The 17 Goals*. https://sdgs.un.org/goals

## Code Attribution

No external code repository, copied online project, or third-party template was used in this project.

All Python code was written specifically for this formative assessment using standard Python concepts taught in the module.

## AI Assistance Disclosure

AI assistance was used as a learning and development support tool. It helped the team understand the assessment brief, interpret the rubric, plan the project structure, divide team responsibilities, improve code comments, explain Python concepts, and draft documentation.

AI support was used for:

- Understanding the formative assessment requirements.
- Selecting the Community Outreach Activity Logger scenario.
- Connecting the project to GCGO and global challenge themes.
- Planning the file structure.
- Explaining JSON file persistence.
- Explaining validation and defensive coding.
- Improving beginner-friendly code comments.
- Suggesting additional features such as report export, top volunteer report, archive option, and confirmation before delete.
- Drafting this Sources and AI Disclosure document.

The team reviewed, adapted, and tested the work to ensure that the final submission is understandable and appropriate for the module level.

## Responsibility Statement

We confirm that we understand the code and can explain how the application works. We can describe the menu system, JSON storage, validation functions, search/filter logic, reporting functions, and file export feature during the project demonstration.

We also confirm that the final submitted project uses Python standard library features only and does not use a database, graphical user interface, or object-oriented class design.
