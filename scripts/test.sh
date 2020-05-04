#!/bin/bash
# Activate virtual environment
#python3 -m virtualenv --python=/usr/bin/python3 /opt/venv
. /opt/venv/bin/activate

# Download requirements to build cache
pip download -d /build -r requirements_test.txt --no-input

# Install application test requirements
pip install --no-index -f /build -r requirements_test.txt

# Run test.sh arguments
exec $@
