#!/bin/bash

set -e

./generate.sh

python3 -m unittest discover \
	-s api_tests \
	-p "*_test.py"
