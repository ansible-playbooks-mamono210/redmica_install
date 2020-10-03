[![](https://github.com/ansible-playbooks-centos7/redmica_install/workflows/ansible-lint/badge.svg)](https://github.com/ansible-playbooks-centos7/redmica_install/actions?query=workflow%3Aansible-lint)
[![](https://github.com/ansible-playbooks-centos7/redmica_install/workflows/molecule/badge.svg)](https://github.com/ansible-playbooks-centos7/redmica_install/actions?query=workflow%3Amolecule)
[![](https://github.com/ansible-playbooks-centos7/redmica_install/workflows/trailing%20whitespace/badge.svg)](https://github.com/ansible-playbooks-centos7/redmica_install/actions?query=workflow%3A%22trailing+whitespace%22)
[![](https://github.com/ansible-playbooks-centos7/redmica_install/workflows/yamllint/badge.svg)](https://github.com/ansible-playbooks-centos7/redmica_install/actions?query=workflow%3Ayamllint)
[![CircleCI](https://circleci.com/gh/ansible-playbooks-centos7/redmica_install.svg?style=svg)](https://circleci.com/gh/ansible-playbooks-centos7/redmica_install)


This playbook installs Redmica on CentOS7.

## Install Redmica

Change to root and execute commands below.

```
ansible-galaxy install -r requirements.yml
ansible-playbook -i localhost, -c local install.yml
```


