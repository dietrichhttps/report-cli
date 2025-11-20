from tabulate import tabulate
from .base import Report
from typing import List
from ..models import Employee


class SummaryReport(Report):
    name = "summary"

    def generate(self, employees: List[Employee]) -> str:
        if not employees:
            return "Нет данных о сотрудниках."

        total = len(employees)

        # Средняя эффективность по всей компании
        avg_perf = round(sum(e.performance for e in employees) / total, 2)

        # Количество уникальных позиций и команд
        positions = len({e.position for e in employees})
        teams = len({e.team for e in employees if e.team.strip()})

        # Среднее количество задач
        avg_tasks = round(sum(e.completed_tasks for e in employees) / total, 1)

        # Средний стаж
        avg_exp = round(sum(e.experience_years for e in employees) / total, 1)

        # Топ-3 самых частых навыка
        skills_count = {}
        for emp in employees:
            for skill in [s.strip() for s in emp.skills.split(",")]:
                if skill:
                    skills_count[skill] = skills_count.get(skill, 0) + 1

        top_skills = sorted(skills_count.items(), key=lambda x: x[1], reverse=True)[:3]
        top_skills_str = ", ".join(f"{skill} ({count})" for skill, count in top_skills)

        # Формируем таблицу
        data = [
            ["Всего сотрудников", total],
            ["Уникальных позиций", positions],
            ["Уникальных команд", teams],
            ["Средняя эффективность", avg_perf],
            ["Среднее задач на человека", avg_tasks],
            ["Средний стаж, лет", avg_exp],
            ["Топ-3 навыка", top_skills_str or "—"],
        ]

        return tabulate(data, headers=["Параметр", "Значение"], tablefmt="grid")