"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["python27", "python36"])
def test_python_amazon(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "amzn":
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python", "python3"])
def test_python_debian(host, pkg):
    """Test that the appropriate packages were installed."""
    if (
        host.system_info.distribution == "debian"
        or host.system_info.distribution == "kali"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python2", "python3"])
def test_python_fedora(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "fedora":
        assert host.package(pkg).is_installed
