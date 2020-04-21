"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["python3"])
def test_python(host, pkg):
    """Test that the appropriate packages were installed."""
    if (
        (
            host.system_info.distribution == "debian"
            and host.system_info.release != "9.12"
        )
        or host.system_info.distribution == "redhat"
        or host.system_info.distribution == "kali"
        or host.system_info.distribution == "amzn"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python", "python3"])
def test_python_debian_9(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "debian" and host.system_info.release == "9.12":
        assert host.package(pkg).is_installed
