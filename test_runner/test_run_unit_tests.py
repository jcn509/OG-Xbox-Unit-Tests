"""Basic runner for Unity unit tests"""
import os
import re
from typing import Optional, Tuple

import git
import pytest

from pyxboxtest.xqemu import XQEMUNetworkForwardRule, XQEMURAMSize, XQEMUXboxAppRunner
from pyxboxtest.xqemu.hdd import XQEMUHDDTemplate


def run_unit_tests(
    hdd_filename: Optional[str] = None,
    dvd_filename: Optional[str] = None,
    network_forward_rules: Optional[Tuple[XQEMUNetworkForwardRule, ...]] = None,
    ram_size: XQEMURAMSize = XQEMURAMSize.RAM128m,
):
    status_line_regex = re.compile(r"(\d+) Tests (\d+) Failures (\d+) Ignored")
    with XQEMUXboxAppRunner(
        hdd_filename=hdd_filename,
        dvd_filename=dvd_filename,
        network_forward_rules=network_forward_rules,
        ram_size=ram_size,
        force_headless=True,
    ) as unit_test_app:
        kernel_debug = unit_test_app.get_kd_capturer()
        line = kernel_debug.get_line()
        status_info = False

        output = line

        while line != "Xbox Unity tests are complete!\n":
            output += line
            if status_info:
                if status_line_regex.match(line):
                    raise RuntimeError("Found 2 status lines - no idea what to do!")
            else:
                status_info = status_line_regex.match(line)
            line = kernel_debug.get_line()

        print("Test runner output:\n" + output)
        assert status_info, "Status line found"
        assert status_info[2] == "0", "No tests failed"


def test_run_unit_tests(xqemu_blank_hdd_template: XQEMUHDDTemplate):
    repo = git.Repo(".", search_parent_directories=True)
    run_unit_tests(
        hdd_filename=xqemu_blank_hdd_template.create_fresh_hdd(),
        dvd_filename=os.path.join(repo.working_tree_dir, "OGXboxUnitTestsExample.iso"),
    )
