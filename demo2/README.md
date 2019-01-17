

## Demo Setup

```bash
python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

virl up --provision
virl generate ansible
```

### Install OpenConfig on Nexus

https://devhub.cisco.com/artifactory/open-nxos-agents/9.2.2/x86_64/

```
feature bash-shell
feature netconf
feature scp-server
```
