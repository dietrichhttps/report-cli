from unittest.mock import patch
import pytest
from report_cli.main import main

def test_unknown_report_exits_with_error(sample1_path):
    with patch("sys.argv", ["main.py", "--files", sample1_path, "--report", "unknown666"]):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 1

def test_file_not_found_exits_with_error():
    with patch("sys.argv", ["main.py", "--files", "not_exists.csv", "--report", "performance"]):
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code == 1