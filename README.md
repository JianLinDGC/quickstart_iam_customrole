## Quickstart IAM API for custom roles

This quickstart can be used as template for get and create roles.

## Requirements

- Have a service account key (name it `key.json` and add it to config/credentials/)

- For creating a new role, the service account needs the iam.roles.create permission

- Activate Identity and Access Management (IAM) API in the Google Cloud Platform console

- Python3 (https://www.python.org/downloads/windows/)

- Python virtualenv and pip installed

- Update PROJECT_NAME in config file

## Setup

```bash
# Create virtualenv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install requirements
pip install --upgrade google-api-python-client google-auth google-auth-httplib2
```

## Documentation

Link to the IAM API documentation: https://cloud.google.com/iam/docs/reference/rest

Role stages: https://cloud.google.com/iam/docs/reference/rest/v1/organizations.roles#Role.RoleLaunchStage
