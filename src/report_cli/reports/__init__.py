from .performance import PerformanceReport
from .summary import SummaryReport

AVAILABLE_REPORTS = {
    "performance": PerformanceReport(),
    "summary": SummaryReport(),
}