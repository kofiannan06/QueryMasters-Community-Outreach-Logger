COMMUNITY  OUTREACH ACTIVITY LOGGGER

1.PROBLEM STATEMENT

Community outreach activities may contain alot of necessary information needed to be kept for referrence. The outreach activities involve multiple volunteers, locations, dates , GCGO themes, hours contributed , and the people reached . Without a well organized system to record this information , it can become difficult to track participation, monitor activities , and understand the impact of outreach efforts.
The Community Outreach A ctivity Logger aims to provide a simple command-line system for recording, managing , and analysing outreach activities.

2.FUNCTIONAL REQUIREMENTS

The application should allow users to :

1.View all recorded outreach activities.
2.Add a new outreach activity.
3.Update an existing  outreach activity.
4.Delete or archive an outreach activity.
5.Search and filter outreach activities.
6.Generate reports from the stored data.
7.Save activity records to a JSON  file.
8.Load previously saved records when the application starts.
9.Validate user input before storing records.
10.Handle invalid input and file errors without crashing.


3. DATA FIELDS

Each outreach activity will be represented as a dictionary containing the following fields:

FIELD         -     PURPOSE

activity_id   -    Unique identifier for the activity
activity_name -    Name of the outreach activity
gcgo_theme    -    GCGO theme associated with the activity
location      -    Location of the activity
date          -    Date  on which the activity occurred 
volunteer_name-    Name of the volunteers
hours_contributed- Number of hours contributed 
people_reached -   Number of people the outreach reached 
status         -Activity status
notes         - Additional information about the activity.


4.VALIDATION REQUIREMENTS

The application should  validate the following inputs:

-Required text fields must not be empty.
-Dates should follow the YYYY-MM-DD format.
-Hours contributed must be a positive number.
-People reached must be a zero or a positive number.
-Status must be one of :
  planned
  completed
  cancelled


