import argparse
import sys

from pip._internal.utils.misc import tabulate

from src.app.runner import ReportRunner
from src.domain.constants import CLI_ARG_FILES, CLI_ARG_REPORT
from src.domain.enums import ExitCode
from src.domain.exceptions import ReportNotFoundError, BaseReportError


def run_cli() -> int:
    parser = argparse.ArgumentParser(description="Student Report Tool")
    parser.add_argument(CLI_ARG_FILES, nargs="+", required=True, dest="files")
    parser.add_argument(CLI_ARG_REPORT, default=True, dest="report")
    args = parser.parse_args()

    try:
        result = ReportRunner.run(args.files, args.report)
        print(tabulate(result.data, headers=result.headers, tablefmt="fancy_grid"))

        return ExitCode.SUCCESS

    except BaseReportError as e:
        print(f"Error: {e}", file=sys.stderr)

        return ExitCode.ERROR

    except Exception as e:
        print(f"Critical error: {e}", file=sys.stderr)

        return ExitCode.CRITICAL

