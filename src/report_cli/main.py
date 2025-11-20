import argparse
import sys
from .data_loader import load_employees_from_files
from .reports import AVAILABLE_REPORTS


def main():
    parser = argparse.ArgumentParser(description="Developer performance reports")
    parser.add_argument("--files", nargs="+", required=True, help="Paths to CSV files")
    parser.add_argument("--report", required=True, help="Report name, e.g. performance")

    args = parser.parse_args()

    if args.report not in AVAILABLE_REPORTS:
        print(f"Unknown report: {args.report}")
        print(f"Available reports: {', '.join(AVAILABLE_REPORTS.keys())}")
        sys.exit(1)

    try:
        employees = load_employees_from_files(args.files)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading files: {e}")
        sys.exit(1)

    report = AVAILABLE_REPORTS[args.report]
    result = report.generate(employees)
    print(result)


if __name__ == "__main__":
    main()