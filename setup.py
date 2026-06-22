import os

# Folders to create
folders = [
    "models",
    "managers",
    "storage",
    "reports",
    "utils",
    "data",
    "logs"
]

# Files to create
files = [
    "main.py",
    "models/expense.py",
    "managers/expense_manager.py",
    "storage/file_handler.py",
    "reports/report_generator.py",
    "utils/validators.py",
    "data/expenses.json",
    "logs/app.log",
    "README.md",
    "requirements.txt"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:

            # Initialize JSON file with empty list
            if file.endswith(".json"):
                f.write("[]")

            # Initialize log file
            elif file.endswith(".log"):
                f.write("Expense Tracker Log File\n")

print("✅ Expense Tracker project structure created successfully!")