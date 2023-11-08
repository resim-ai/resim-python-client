#!/bin/bash

set -e

# Navigate to the parent directory to update
TOPLEVEL=$(git rev-parse --show-toplevel)
pushd "${TOPLEVEL}/.."

URL="https://api.resim.ai/v1/openapi.yaml"
CONFIG="${TOPLEVEL}/openapi_python_client_config.yaml"

openapi-python-client update \
		      --config "${CONFIG}" \
		      --url "${URL}"

popd
