"""Module containing the tests for the default scenario."""

import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkgs", [["python", "python27"], ["python3", "python36"]])
def test_python(host, pkgs):
    """Test that the appropriate packages were installed."""
    packages = [host.package(pkg) for pkg in pkgs]
    installed = [package.is_installed for package in packages]
    assert any(installed)
