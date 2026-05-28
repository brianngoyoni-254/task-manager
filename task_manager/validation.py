from datetime import datetime

def validate_task_title(title):
    if isinstance(title, str) and title.strip() != "":
        return True
    print("Invalid title!")
    return False


def validate_task_description(description):
    if isinstance(description, str) and description.strip() != "":
        return True
    print("Invalid description!")
    return False


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD")
        return False