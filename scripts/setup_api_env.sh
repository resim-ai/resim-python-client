#!/bin/bash

set -e

DIRNAME=api_sandbox
mkdir "${DIRNAME}"
cd "${DIRNAME}"

python3 -m venv .venv

source .venv/bin/activate

pip install pip-tools

echo requirements.txt

cat <<EOF > requirements.txt
resim_open_core @ https://github.com/resim-ai/open-core/releases/download/v0.0.15/resim_open_core-0.0.15-py3-none-manylinux2014_x86_64.whl
resim-python-client @ git+https://github.com/resim-ai/resim-python-client@a28eca31985d175d976b868d38c7f3adc315155b
requests
polling2
h11
EOF

pip-compile -o requirements_lock.txt requirements.txt

pip install -r requirements_lock.txt

cat <<EOF > queries.py
import asyncio

from resim_python_client.client import AuthenticatedClient
from resim.auth.python.device_code_client import DeviceCodeClient

from resim_python_client.api.projects import list_projects
from resim.metrics.fetch_all_pages import async_fetch_all_pages


def get_client():
    api_url = "https://api.resim.ai/v1/"
    auth_url = "https://resim.us.auth0.com"
    client_id = "gTp1Y0kOyQ7QzIo2lZm0auGM6FJZZVvy"

    auth_client = DeviceCodeClient(domain=auth_url, client_id=client_id)
    token = auth_client.get_jwt()["access_token"]
    client = AuthenticatedClient(base_url=api_url, token=token)
    return client


async def main():
    client = get_client()
    project_pages = await async_fetch_all_pages(list_projects.asyncio, client=client)
    projects = [e for page in project_pages for e in page.projects]
    print("Projects:")
    for project in projects:
        print(f"  {project.name}")

    # Add your queries here


if __name__ == "__main__":
    asyncio.run(main())
EOF
