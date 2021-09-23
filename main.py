from app.services.iam import IamService
from config import SERVICE_ACCOUNT_ADMIN_ROLE, IAM_ROLES_GET_PERMISSION, PROJECT_NAME


def main():
    iam_service = IamService()

    ## Examples
    # Get a role
    role = iam_service.get_role(SERVICE_ACCOUNT_ADMIN_ROLE)
    print(role)

    # Create custom role
    permissions = [IAM_ROLES_GET_PERMISSION]
    new_role = iam_service.create_role(
        name='CustomRoleId',
        project=PROJECT_NAME,
        title='My Custom Role',
        description='My description',
        permissions=permissions,
        stage='GA'
    )
    print(new_role)


if __name__ == '__main__':
    main()
