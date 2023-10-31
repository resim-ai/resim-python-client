#!/bin/bash

set -e

URL="https://api.resim.ai/v1/openapi.yaml"
CONFIG="openapi_python_client_config.yaml"

openapi-python-client generate \
		      --config "${CONFIG}" \
		      --url "${URL}"

