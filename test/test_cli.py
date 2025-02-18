from unittest.mock import patch
from bitbucket_cli.cli import BitbucketCLI

@patch("bitbucket_cli.api.BitbucketAPI.create_project")
def test_create_project(mock_create_project):
    cli = BitbucketCLI()
    args = type("Args", (), {"workspace": "myworkspace", "name": "My Project", "key": "MYPROJ"})
    cli.create_project(args)
    mock_create_project.assert_called_once_with("myworkspace", "My Project", "MYPROJ")

@patch("bitbucket_cli.api.BitbucketAPI.create_repo")
def test_create_repo(mock_create_repo):
    cli = BitbucketCLI()
    args = type("Args", (), {"workspace": "myworkspace", "project_key": "MYPROJ", "name": "my-repo"})
    cli.create_repo(args)
    mock_create_repo.assert_called_once_with("myworkspace", "MYPROJ", "my-repo")