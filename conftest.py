# conftest.py
import datetime
from pathlib import Path
import os

def pytest_configure(config):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    environment = os.getenv("TEST_ENV") or (
        "docker" if Path("/.dockerenv").exists() else "local"
    )
    report_dir = f"test-reports/{environment}"
    Path(report_dir).mkdir(parents=True, exist_ok=True)
    report_file = f"{report_dir}/report_{timestamp}.html"
    config.option.htmlpath = report_file
