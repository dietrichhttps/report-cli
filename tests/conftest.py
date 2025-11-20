import pytest
from pathlib import Path

@pytest.fixture
def fixtures_dir():
    return Path(__file__).parent / "fixtures"

@pytest.fixture
def sample1_path(fixtures_dir):
    return str(fixtures_dir / "sample1.csv")

@pytest.fixture
def sample2_path(fixtures_dir):
    return str(fixtures_dir / "sample2.csv")