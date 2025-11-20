import csv
from typing import List
from .models import Employee

def load_employees_from_files(file_paths: List[str]) -> List[Employee]:
    employees = []
    for path in file_paths:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                emp = Employee(
                    name=row['name'],
                    position=row['position'],
                    completed_tasks=int(row['completed_tasks']),
                    performance=float(row['performance']),
                    skills=row['skills'],
                    team=row['team'],
                    experience_years=int(row['experience_years']),
                )
                employees.append(emp)
    return employees