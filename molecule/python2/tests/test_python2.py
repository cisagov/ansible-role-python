"""Module containing the tests for the python2 scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_python2_packages(host):
    """Test that the appropriate Python 2 packages were installed."""
    if host.system_info.distribution in ["amzn"]:
        for p in ["python", "python2-rpm"]:
            assert host.package(p).is_installed
    elif host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        if host.system_info.codename in ["bionic", "stretch"]:
            for p in ["python", "python-apt", "python-minimal"]:
                assert host.package(p).is_installed
        elif host.system_info.codename in ["buster"]:
            for p in ["python2", "python-apt", "python2-minimal"]:
                assert host.package(p).is_installed
        else:
            for p in ["python2", "python2-minimal"]:
                assert host.package(p).is_installed
    elif host.system_info.distribution in ["fedora"]:
        for p in ["python2.7"]:
            assert host.package(p).is_installed
    else:
        assert (
            False
        ), f"Linux distribution {host.system_info.distribution} is not supported."
