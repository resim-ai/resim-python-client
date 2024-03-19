# resim-python-client

This repository contains code for generating and distributing a python
client for ReSim's API.

## Regenerating the Client

In order to regenerate the client, one needs to install the openapi-python-client:

```
pipx install openapi-python-client --include-deps
```

Then, run `.generate.sh`. If you are generating a python client that is in front of the deployed ReRun API,
then one needs to change `.generate.sh` to use the `--path` parameter and then supply a path to an API 
specification.