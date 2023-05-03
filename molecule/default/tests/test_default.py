"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_python3_packages(host):
    """Test that the appropriate Python 3 packages were installed."""
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        for p in ["python3", "python3-apt", "python3-minimal"]:
            assert host.package(p).is_installed
    elif host.system_info.distribution in ["amzn", "fedora"]:
        for p in ["python3", "python3-dnf"]:
            assert host.package(p).is_installed
    else:
        assert (
            False
        ), f"Linux distribution {host.system_info.distribution} is not supported."
