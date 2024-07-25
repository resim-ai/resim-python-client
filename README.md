# resim-python-client

This repository contains code for generating and distributing a python
client for ReSim's API.

## Regenerating the Client

In order to regenerate the client, one needs to install the openapi-python-client:

```
pipx install openapi-python-client --include-deps
```

Then, run `./generate.sh`. If you are generating a python client that is in front of the deployed ReRun API,
then one needs to change `generate.sh` to use the `--path` parameter and then supply a path to an API 
specification.

## Quickstart

If you want to quickly start querying the API, you can use our
`setup_api_env.sh` script to set up a local environment which uses the device
code flow to authenticate. If you get authentication issues, you may have to
manually delete the contents of `~/.resim/`. To set up such an environment, you
can do the following:

```bash
curl -s https://raw.githubusercontent.com/resim-ai/resim-python-client/main/scripts/setup_api_env.sh | bash
cd api_sandbox/
source .venv/bin/activate

# Run the entypoint which prints out the projects for your organization
python queries.py
```
