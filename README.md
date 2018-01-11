# BRKDEV-1368

# Environment Setup

Follow these instructions to standup the demo and code environment.  

1. Pre-reqs
  * Python 2.7 and Python 3.6
    * pip and virtualenv
  * Vagrant
  * VirtualBox

1. Setup Python Virtual Environment

  ```bash
  virtualenv venv --python=python2.7
  source venv/bin/activate
  pip install requirements.txt
  ```

1. Vagrant Up the environment

  ```bash
  vagrant up
  ```

  * Should the Ansible provisioning error out due to "shell connection".  Re run the provisioner and restart.  

    ```bash
    vagrant provision
    vagrant up
    ```

  * Repeat the above if/as needed until `vagant up` reports fully successful
