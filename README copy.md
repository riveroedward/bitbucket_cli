Description
This Python module provides a wrapper for interacting with the Bitbucket API. It simplifies the process of managing Bitbucket workspaces, projects, repositories, user permissions, and branch restrictions.

Requirements
Python 3.x
requests library
Install the required package with:

bash
Copiar
Editar
pip install requests

Configuration
This module relies on a separate configuration file, config.py, which should define the following variables:

python
Copiar
Editar
class Config:
    BITBUCKET_API_URL = "https://api.bitbucket.org/2.0"
    BITBUCKET_USERNAME = "your_bitbucket_username"
    BITBUCKET_ACCESS_TOKEN = "your_bitbucket_access_token"

Class: BitbucketAPI
def __init__(self):


Initializes the BitbucketAPI object with HTTP Basic Authentication using the username and access token from the Config class.

Methods
1. create_project(workspace, project_name, project_key)
Creates a new project in the specified Bitbucket workspace.

Parameters:

workspace (str): The workspace ID where the project will be created.
project_name (str): The name of the new project.
project_key (str): A unique key for the project (e.g., an abbreviation).

2. create_repo(workspace, project_key, repo_name)
Creates a new repository within a project in the specified workspace.

Parameters:

workspace (str): The workspace ID.
project_key (str): The key of the project to associate with the repository.
repo_name (str): The name of the new repository.

3. add_user_to_repo(workspace, repo_slug, username, permission)
Adds a user to a repository with the specified permission level.

Parameters:

workspace (str): The workspace ID.
repo_slug (str): The repository slug (name).
username (str): The Bitbucket username to be added.
permission (str): Permission level (read, write, or admin).

remove_user_from_repo(workspace, repo_slug, username)
Removes a user from a repository's permission list.

Parameters:

workspace (str): The workspace ID.
repo_slug (str): The repository slug (name).
username (str): The Bitbucket username to be removed.

5. configure_branch_permissions(workspace, repo_slug, branch_name, exempt_users)
Configures branch restrictions to require pull requests for merging, with optional exemptions for specific users.

Parameters:

workspace (str): The workspace ID.
repo_slug (str): The repository slug (name).
branch_name (str): The branch pattern to apply restrictions to.
exempt_users (list): List of usernames exempt from the restriction.


BitbucketCLI Python Tool
Description
This Python CLI tool provides a command-line interface for managing Bitbucket projects, repositories, and user permissions using the Bitbucket API. It allows you to:

Create projects and repositories
Manage user permissions
Configure branch restrictions
Requirements
Python 3.x
requests library
Install the required package with:

bash
Copiar
Editar
pip install requests
Configuration
This tool relies on a configuration file (config.py) that should define the following variables:

python
Copiar
Editar
class Config:
    BITBUCKET_API_URL = "https://api.bitbucket.org/2.0"
    BITBUCKET_USERNAME = "your_bitbucket_username"
    BITBUCKET_ACCESS_TOKEN = "your_bitbucket_access_token"

    @staticmethod
    def validate():
        if not all([Config.BITBUCKET_API_URL, Config.BITBUCKET_USERNAME, Config.BITBUCKET_ACCESS_TOKEN]):
            raise ValueError("Please set all required configuration variables.")
Usage
The tool provides several commands for interacting with Bitbucket. Each command uses subparsers to handle different actions.

1. Create Project
Creates a new project in a specified workspace.

bash
Copiar
Editar
python cli.py create-project --workspace <workspace> --name <project_name> --key <project_key>
Parameters:

--workspace: The Bitbucket workspace ID.
--name: The name of the new project.
--key: A unique key for the project (e.g., an abbreviation).
Example:

bash
Copiar
Editar
python cli.py create-project --workspace my_workspace --name "New Project" --key NP
2. Create Repository
Creates a new repository within an existing project in the specified workspace.

bash
Copiar
Editar
python cli.py create-repo --workspace <workspace> --project-key <project_key> --name <repo_name>
Parameters:

--workspace: The Bitbucket workspace ID.
--project-key: The project key to associate with the repository.
--name: The name of the new repository.
Example:

bash
Copiar
Editar
python cli.py create-repo --workspace my_workspace --project-key NP --name new-repo
3. Add User to Repository
Adds a user to a repository with the specified permission level.

bash
Copiar
Editar
python cli.py add-user --workspace <workspace> --repo-slug <repo_slug> --username <username> --permission <permission>
Parameters:

--workspace: The Bitbucket workspace ID.
--repo-slug: The repository slug (name).
--username: The Bitbucket username to add.
--permission: Permission level (read, write, or admin).
Example:

bash
Copiar
Editar
python cli.py add-user --workspace my_workspace --repo-slug new-repo --username user123 --permission write
4. Remove User from Repository
Removes a user from a repository's permission list.

bash
Copiar
Editar
python cli.py remove-user --workspace <workspace> --repo-slug <repo_slug> --username <username>
Parameters:

--workspace: The Bitbucket workspace ID.
--repo-slug: The repository slug (name).
--username: The Bitbucket username to remove.
Example:

bash
Copiar
Editar
python cli.py remove-user --workspace my_workspace --repo-slug new-repo --username user123
5. Configure Branch Permissions
Configures branch restrictions to require pull requests for merging, with optional exemptions for specific users.

bash
Copiar
Editar
python cli.py configure-branch --workspace <workspace> --repo-slug <repo_slug> --branch-name <branch_name> --exempt-users <exempt_users>
Parameters:

--workspace: The Bitbucket workspace ID.
--repo-slug: The repository slug (name).
--branch-name: The branch pattern to apply restrictions to.
--exempt-users: Space-separated list of usernames exempt from the restriction.
Example:

bash
Copiar
Editar
python cli.py configure-branch --workspace my_workspace --repo-slug new-repo --branch-name main --exempt-users user1 user2
Error Handling
The tool uses try-except blocks to catch exceptions and log errors using log_error.
Informational messages are logged with log_info.
Logging
This tool relies on utility functions log_error() and log_info() from the utils module for logging purposes. Ensure these functions are implemented for proper logging.

Example:

python
Copiar
Editar
def log_info(message):
    print(f"[INFO] {message}")

def log_error(message):
    print(f"[ERROR] {message}")
Example Execution
bash
Copiar
Editar
python cli.py create-project --workspace my_workspace --name "New Project" --key NP
python cli.py create-repo --workspace my_workspace --project-key NP --name new-repo
python cli.py add-user --workspace my_workspace --repo-slug new-repo --username user123 --permission write
python cli.py configure-branch --workspace my_workspace --repo-slug new-repo --branch-name main --exempt-users user1 user2
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
[Your Name] - [Your Contact Information]

Acknowledgments
Bitbucket API Documentation
Feel free to modify this README to better suit your project requirements!
s







