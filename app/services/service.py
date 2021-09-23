from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config import (
    SERVICE_ACCOUNT_KEY_FILE,
    SCOPES
)


class Service:
    """Service builder"""

    def __init__(self, service_name, version):
        self.service_name = service_name
        self.version = version
        self.credentials = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_KEY_FILE,
            scopes=SCOPES
        )
        self.service = self.build(self.service_name, self.version)

    def build(self, service, version):
        """build the service from name, version and credentials"""
        return build(
            service, 
            version, 
            credentials=self.credentials
        )
