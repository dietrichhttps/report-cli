import pytest

from report_cli.data_loader import load_employees_from_files
from report_cli.models import Employee

def test_load_single_file(sample1_path):
    employees = load_employees_from_files([sample1_path])
    assert len(employees) == 9
    assert isinstance(employees[0], Employee)
    assert employees[0].name == "David Chen"
    assert employees[0].performance == 4.6

def test_load_multiple_files(sample1_path, sample2_path):
    employees = load_employees_from_files([sample1_path, sample2_path])
    assert len(employees) == 15
    positions = {e.position for e in employees}
    assert "Backend Developer" in positions
    assert "Data Scientist" in positions

def test_load_nonexistent_file(tmp_path):
    fake_path = str(tmp_path / "not_exists.csv")
    with pytest.raises(FileNotFoundError):
        load_employees_from_files([fake_path])