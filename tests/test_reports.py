import pytest
from report_cli.reports.performance import PerformanceReport
from report_cli.reports.summary import SummaryReport
from report_cli.data_loader import load_employees_from_files

@pytest.fixture
def employees(sample1_path, sample2_path):
    return load_employees_from_files([sample1_path, sample2_path])

def test_performance_report(employees):
    report = PerformanceReport()
    output = report.generate(employees)

    assert "Avg Performance" in output
    assert "Backend Developer" in output
    # Первая строка после заголовка — самая высокая эффективность
    lines = output.splitlines()
    assert "4.83" in lines[3]  # предположим, что бэкендеры лидируют

# tests/test_reports.py

def test_performance_report_sorting(employees):
    """Проверяем, что отчёт performance сортирует позиции по убыванию средней эффективности"""
    report = PerformanceReport()
    output = report.generate(employees)

    # Ищем строки с данными (те, что содержат "│" и число с точкой)
    perf_values = []
    for line in output.splitlines():
        if "│" in line and "." in line:
            parts = [p.strip() for p in line.split("│") if p.strip()]
            if len(parts) >= 2:
                try:
                    value = float(parts[-1])  # последнее — это Avg Performance
                    perf_values.append(value)
                except ValueError:
                    continue

    # Теперь проверяем, что значения идут по убыванию
    assert perf_values == sorted(perf_values, reverse=True), \
        f"Значения не отсортированы по убыванию: {perf_values}"

def test_summary_report(employees):
    report = SummaryReport()
    output = report.generate(employees)

    assert "Всего сотрудников" in output
    assert "15" in output
    assert "Средняя эффективность" in output
    assert "Топ-3 навыка" in output
    assert "Python" in output

def test_summary_empty_data():
    report = SummaryReport()
    output = report.generate([])
    assert "Нет данных" in output