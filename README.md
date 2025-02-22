# Bitbucket CLI

_Project Overview_

Bitbucket CLI is a command-line tool designed to interact with Bitbucket's API, allowing users to efficiently manage repositories, pull requests, and other resources without leaving the terminal.

### File Structure

_Here's an overview of the project's files and directories:

### .env: 

Configuration file for environment variables. It stores sensitive information like Bitbucket credentials.


 ###  main.py: 

 The main entry point of the CLI tool. It initializes the application and parses command-line arguments.

### requirements.txt: 

Lists all Python dependencies required to run the project.

# bitbucket_cli/: Contains the core modules of the project:

### api.py: 

_Manages all interactions with the Bitbucket API, including authentication, listing repositories, and managing pull requests._

### cli.py: 

_Handles the command-line interface, parsing user input, and calling appropriate functions from api.py._

### config.py: 

_Manages configuration settings, including loading environment variables from .env._

### utils.py: 

_Utility functions shared across different modules, like data formatting and error handling._

### test/: 

_Contains unit tests for the application:_

### init.py: 

_Marks the directory as a package._

### test_api.py: 
_Unit tests for the api.py module._

### test_cli.py: 

_Unit tests for the cli.py module._

### Features
```
_List, create, and manage repositories_
```
View and manage pull requests

## Interact with branches and commits

_Configurable through a .env file_

### Installation

Clone the repository:
```
git clone <repository-url>
cd bitbucket_cli-main
```
Create and activate a virtual environment (optional but recommended):
```
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
Install the required dependencies:
```
pip install -r requirements.txt
```
### Configuration

_Create a .env file in the root directory and provide your Bitbucket credentials and other necessary configurations_

```
BITBUCKET_USERNAME=<your-username>
BITBUCKET_ACCESS_TOKEND=<your-token>
```
Usage

To start using the CLI tool, run:
```
python main.py --help
```
Example commands:
```
python main.py create-project --workspace myworkspaces --name "My Project" --key MYPROJ
python main.py create-repo --workspace myworkspace --project-key MYPROJ --name my-repo
python3 main.py add-user --workspace myworkspacesr --repo-slug my-repo --username <username> --permission write
python main.py configure-branch --workspace myworkspace --repo-slug my-repo --branch-name main --exempt-users edw.riv
```
### Testing

_To run the tests, use the following command:_
```
pytest test/
```
