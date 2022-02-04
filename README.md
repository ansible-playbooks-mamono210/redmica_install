[![](https://github.com/ansible-playbooks-mamono210/redmica_install/workflows/build/badge.svg)](https://github.com/ansible-playbooks-mamono210/redmica_install/actions?query=workflow%3Abuild)
[![CircleCI](https://circleci.com/gh/ansible-playbooks-mamono210/redmica_install.svg?style=svg)](https://circleci.com/gh/ansible-playbooks-mamono210/redmica_install)


This playbook installs Redmica on CentOS Stream 8.

## Install Redmica

Change to root and execute commands below.

```
ansible-galaxy install -r requirements.yml
ansible-playbook -i localhost, -c local install.yml
```
