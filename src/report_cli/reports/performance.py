from collections import defaultdict
from tabulate import tabulate
from .base import Report
from typing import List
from ..models import Employee


class PerformanceReport(Report):
    name = "performance"

    def generate(self, employees: List[Employee]) -> str:
        position_stats = defaultdict(list)

        for emp in employees:
            position_stats[emp.position].append(emp.performance)

        data = []
        for position, perfs in position_stats.items():
            avg_perf = sum(perfs) / len(perfs)
            data.append({"Position": position, "Avg Performance": round(avg_perf, 2)})

        data.sort(key=lambda x: x["Avg Performance"], reverse=True)

        return tabulate(data, headers="keys", tablefmt="grid")