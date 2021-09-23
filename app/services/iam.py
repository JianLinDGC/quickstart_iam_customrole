"""
Iam Client

https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles
"""

import logging

from googleapiclient.errors import HttpError
from app.services.service import Service
from config import IAM_SERVICE_NAME, IAM_API_VERSION


class IamService(Service):
    """IAM Service"""

    def __init__(self):
        Service.__init__(self, IAM_SERVICE_NAME, IAM_API_VERSION)

    def get_role(self, name):
        try:
            role = self.service.roles().get(name=name).execute()
            return role
        except HttpError as err:
            if err.resp.status == 404:
                logging.error("Role %s not found", name)
            else:
                logging.error("Error getting role %s: %s", name, str(err))

    def get_custom_role(self, name):
        # Custom role name regex format: ^projects/[^/]+/roles/[^/]+$
        try:
            role = self.service.projects().roles().get(name=name).execute()
            return role
        except HttpError as err:
            if err.resp.status == 404:
                logging.error("Custom Role %s not found", name)
            else:
                logging.error("Error getting role %s: %s", name, str(err))

    def create_role(self, name, project, title, description, permissions, stage):
        try:
            role = self.service.projects().roles().create(
                parent='projects/' + project,
                body = {
                    'roleId': name,
                    'role': {
                        'title': title,
                        'description': description,
                        'includedPermissions': permissions,
                        'stage': stage
                    }
                }).execute()
            return role
        except HttpError as err:
            logging.error("Error creating role %s: %s", name, err)
