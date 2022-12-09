# ansible-role-python #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-python/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-python/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-python/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-python/actions/workflows/codeql-analysis.yml)

An Ansible role for installing [Python](https://www.python.org/).

## Requirements ##

This role uses the `package` Ansible module, so [its
requirements](https://docs.ansible.com/ansible/latest/modules/package_module.html#requirements)
apply.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| install_python2 | A boolean indicating whether or not to install Python 2 alongside Python 3.  Where possible, we also install the necessary dependencies to use Python 2 as Ansible's discovered Python; unfortunately, this is only possible on Amazon Linux 2, Debian Stretch, Debian Buster, and Ubuntu Bionic. | `false` | No |

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  tasks:
    - name: Install python
      ansible.builtin.include_role:
        name: python
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
