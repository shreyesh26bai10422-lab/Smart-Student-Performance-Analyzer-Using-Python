# Design Notes

Architecture:
User -> main.py -> functional modules -> CSV/simple data -> report/output

Workflow:
1. User selects an option.
2. Program validates input.
3. A module processes the data.
4. Data is stored/read from a simple file when needed.
5. The result is displayed to the user.

Three major modules:
- Student Data Management
- Performance Calculation
- Analysis & Report
