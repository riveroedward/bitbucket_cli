**Bitbucket CLI**

Project Overview

Bitbucket CLI is a command-line tool designed to interact with Bitbucket's API, allowing users to efficiently manage repositories, pull requests, and other resources without leaving the terminal.

File Structure

Here's an overview of the project's files and directories:

.env: Configuration file for environment variables. It stores sensitive information like Bitbucket credentials.

README.md: Documentation file providing an overview, installation, and usage instructions.

main.py: The main entry point of the CLI tool. It initializes the application and parses command-line arguments.

requirements.txt: Lists all Python dependencies required to run the project.

bitbucket_cli/: Contains the core modules of the project:

api.py: Manages all interactions with the Bitbucket API, including authentication, listing repositories, and managing pull requests.

cli.py: Handles the command-line interface, parsing user input, and calling appropriate functions from api.py.

config.py: Manages configuration settings, including loading environment variables from .env.

utils.py: Utility functions shared across different modules, like data formatting and error handling.

test/: Contains unit tests for the application:

init.py: Marks the directory as a package.

test_api.py: Unit tests for the api.py module.

test_cli.py: Unit tests for the cli.py module.

Features

List, create, and manage repositories

View and manage pull requests

Interact with branches and commits

Configurable through a .env file

Installation

Clone the repository:

git clone <repository-url>
cd bitbucket_cli-main

Create and activate a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

Install the required dependencies:

pip install -r requirements.txt

Configuration

Create a .env file in the root directory and provide your Bitbucket credentials and other necessary configurations:

BITBUCKET_USERNAME=<your-username>
BITBUCKET_ACCESS_TOKEND=<your-token>

Usage

To start using the CLI tool, run:

python main.py --help

Example commands:

python main.py list-repos
python main.py create-repo --name <repo-name>

Testing

To run the tests, use the following command:

pytest test/

