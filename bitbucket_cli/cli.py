import argparse
from .api import BitbucketAPI
from .config import Config
from .utils import log_error, log_info

class BitbucketCLI:
    def __init__(self):
        self.api = BitbucketAPI()

    def create_project(self, args):
        try:
            self.api.create_project(args.workspace, args.name, args.key)
            log_info(f"Project '{args.name}' created successfully.")
        except Exception as e:
            log_error(f"Failed to create project: {e}")

    def create_repo(self, args):
        try:
            self.api.create_repo(args.workspace, args.project_key, args.name)
            log_info(f"Repository '{args.name}' created successfully.")
        except Exception as e:
            log_error(f"Failed to create repository: {e}")

    def add_user(self, args):
        try:
            self.api.add_user_to_repo(args.workspace, args.repo_slug, args.username, args.permission)
            log_info(f"User '{args.username}' added to repository '{args.repo_slug}' with '{args.permission}' permission.")
        except Exception as e:
            log_error(f"Failed to add user: {e}")

    def remove_user(self, args):
        try:
            self.api.remove_user_from_repo(args.workspace, args.repo_slug, args.username)
            log_info(f"User '{args.username}' removed from repository '{args.repo_slug}'.")
        except Exception as e:
            log_error(f"Failed to remove user: {e}")

    def configure_branch(self, args):
        try:
            self.api.configure_branch_permissions(args.workspace, args.repo_slug, args.branch_name, args.exempt_users)
            log_info(f"Branch permissions configured for '{args.branch_name}'.")
        except Exception as e:
            log_error(f"Failed to configure branch permissions: {e}")

def main():
    Config.validate()
    cli = BitbucketCLI()
    parser = argparse.ArgumentParser(description="Bitbucket CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Create project
    create_project_parser = subparsers.add_parser("create-project", help="Create a new project")
    create_project_parser.add_argument("--workspace", required=True, help="Bitbucket workspace")
    create_project_parser.add_argument("--name", required=True, help="Project name")
    create_project_parser.add_argument("--key", required=True, help="Project key")
    create_project_parser.set_defaults(func=cli.create_project)

    # Create repository
    create_repo_parser = subparsers.add_parser("create-repo", help="Create a new repository")
    create_repo_parser.add_argument("--workspace", required=True, help="Bitbucket workspace")
    create_repo_parser.add_argument("--project-key", required=True, help="Project key")
    create_repo_parser.add_argument("--name", required=True, help="Repository name")
    create_repo_parser.set_defaults(func=cli.create_repo)

    # Add user to repository
    add_user_parser = subparsers.add_parser("add-user", help="Add a user to a repository")
    add_user_parser.add_argument("--workspace", required=True, help="Bitbucket workspace")
    add_user_parser.add_argument("--repo-slug", required=True, help="Repository slug")
    add_user_parser.add_argument("--username", required=True, help="Username")
    add_user_parser.add_argument("--permission", required=True, help="Permission level (read, write, admin)")
    add_user_parser.set_defaults(func=cli.add_user)

    # Remove user from repository
    remove_user_parser = subparsers.add_parser("remove-user", help="Remove a user from a repository")
    remove_user_parser.add_argument("--workspace", required=True, help="Bitbucket workspace")
    remove_user_parser.add_argument("--repo-slug", required=True, help="Repository slug")
    remove_user_parser.add_argument("--username", required=True, help="Username")
    remove_user_parser.set_defaults(func=cli.remove_user)

    # Configure branch permissions
    branch_permissions_parser = subparsers.add_parser("configure-branch", help="Configure branch permissions")
    branch_permissions_parser.add_argument("--workspace", required=True, help="Bitbucket workspace")
    branch_permissions_parser.add_argument("--repo-slug", required=True, help="Repository slug")
    branch_permissions_parser.add_argument("--branch-name", required=True, help="Branch name")
    branch_permissions_parser.add_argument("--exempt-users", nargs="+", required=True, help="List of exempt users")
    branch_permissions_parser.set_defaults(func=cli.configure_branch)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
