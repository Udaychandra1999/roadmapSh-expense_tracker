# roadmapSh-expense_tracker

https://roadmap.sh/projects/expense-tracker

# Expense Tracker

A simple command-line expense tracker built with Python.

The application allows you to add, list, delete, and summarize your expenses. Expenses are stored locally in a JSON file, so no external database is required.

## Features

- Add a new expense
- List all expenses
- Delete an expense by ID
- Calculate total expenses
- Calculate expenses for a specific month
- Store data locally using JSON
- Command-line interface using `argparse`
- Single executable can be created using PyInstaller

## Requirements

- Python 3.10+
- Linux / macOS / Windows
- PyInstaller (only required for building the executable)

## Project Structure

```text
expense-tracker/
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── handler.py
│   └── parser.py
├── test/
├── expenses.json
├── main.py
├── .gitignore
├── LICENSE
└── README.md
```

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd expense-tracker
```

Create a virtual environment:

```bash
python3 -m venv expense_tracker_env
```

Activate it:

```bash
source expense_tracker_env/bin/activate
```

No external Python packages are required to run the application.

## Usage

Run the application with:

```bash
python3 main.py
```

Running the application without a command displays the available commands.

### Add an expense

```bash
python3 main.py add --description "Lunch" --amount 20
```

Example:

```text
Expense added successfully (ID: 1)
```

### List expenses

```bash
python3 main.py list
```

Example:

```text
ID   Date           Description              Amount
--------------------------------------------------
1    2026-09-22     Lunch                      $20.00
2    2026-09-22     Bus                         $2.00
```

### Delete an expense

```bash
python3 main.py delete --id 2
```

Example:

```text
Expense id:2 deleted successfully
```

If the ID does not exist:

```text
Expense with id:2 not found
```

### Show expense summary

Show the total of all expenses:

```bash
python3 main.py summary
```

Example:

```text
Total expenses: $22.00
```

Show expenses for a specific month:

```bash
python3 main.py summary --month 9
```

Example:

```text
Total expenses for September: $22.00
```

## Command Help

Display general help:

```bash
python3 main.py --help
```

Display help for a specific command:

```bash
python3 main.py add --help
python3 main.py list --help
python3 main.py delete --help
python3 main.py summary --help
```

## Data Storage

Expenses are stored in:

```text
expenses.json
```

Example:

```json
[
  {
    "id": 1,
    "description": "Lunch",
    "amount": 20.0,
    "date": "2026-09-22"
  }
]
```

The application uses JSON instead of an external database, making it simple to run and easy to inspect the stored data.

## Building a Single Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --name expense-tracker main.py
```

The executable will be created inside:

```text
dist/expense-tracker
```

Run it:

```bash
./dist/expense-tracker
```

For example:

```bash
./dist/expense-tracker add --description "Lunch" --amount 20
```

## Technologies Used

- Python
- argparse
- JSON
- TypedDict
- PyInstaller

## Future Improvements

- Add automated tests
- Improve error handling
- Store the database in a user-specific application directory
- Add expense editing
- Add categories
- Add date filtering
- Improve terminal output
- Package releases for different operating systems

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
