"""Provides unit tests execution script."""

import logging
import subprocess
import sys
from pathlib import Path

from varname import nameof

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    repository_dir_path = Path(__file__).parent.parent
    tests_directory_path = repository_dir_path / "tests"

    logging.debug("%s = %s", nameof(tests_directory_path), tests_directory_path)

    process_result = subprocess.run(
        args=[sys.executable, "-m", "unittest", "discover", tests_directory_path],
        check=True,
    )
