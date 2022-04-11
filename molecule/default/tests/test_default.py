"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["python"])
def test_python(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "debian" and (
        host.system_info.codename == "stretch" or host.system_info.codename == "buster"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python3"])
def test_python3(host, pkg):
    """Test that the appropriate packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python-apt", "python-minimal"])
def test_python_apt(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "debian" and (
        host.system_info.codename == "stretch" or host.system_info.codename == "buster"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python3-apt", "python3-minimal"])
def test_python3_apt(host, pkg):
    """Test that the appropriate packages were installed."""
    if (
        host.system_info.distribution == "debian"
        or host.system_info.distribution == "kali"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python3-dnf"])
def test_python3_dnf(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "redhat":
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python3-rpm"])
def test_python3_rpm(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "amzn":
        assert host.package(pkg).is_installed
