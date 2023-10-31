#!/bin/bash

set -e

./generate.sh
pip3 install ./resim-python-client/

python3 -m unittest discover \
	-s api_tests \
	-p "*_test.py"
