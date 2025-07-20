#!/bin/bash

# Ensure we're in the project directory
cd "$(dirname "$0")"

# Add the current directory to the PYTHONPATH
export PYTHONPATH=$PYTHONPATH:.

# Export test environment variables
export DJANGO_SETTINGS_MODULE=project.settings.test
export SECRET_KEY=test-secret-key-not-for-production

# Run tests with pytest
pytest tests
