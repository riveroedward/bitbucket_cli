import pytest
from unittest.mock import patch, Mock
from bitbucket_cli.api import BitbucketAPI

@pytest.fixture
def mock_api():
    return BitbucketAPI()

@patch("requests.post")
def test_create_project(mock_post, mock_api):
    mock_post.return_value = Mock(status_code=201, json=lambda: {"key": "MYPROJ"})
    response = mock_api.create_project("myworkspace", "My Project", "MYPROJ")
    assert response == {"key": "MYPROJ"}

@patch("requests.post")
def test_create_repo(mock_post, mock_api):
    mock_post.return_value = Mock(status_code=200, json=lambda: {"slug": "my-repo"})
    response = mock_api.create_repo("myworkspace", "MYPROJ", "my-repo")
    assert response == {"slug": "my-repo"}

@patch("requests.put")
def test_add_user_to_repo(mock_put, mock_api):
    mock_put.return_value = Mock(status_code=200, json=lambda: {"username": "john.doe"})
    response = mock_api.add_user_to_repo("myworkspace", "my-repo", "john.doe", "write")
    assert response == {"username": "john.doe"}

@patch("requests.delete")
def test_remove_user_from_repo(mock_delete, mock_api):
    mock_delete.return_value = Mock(status_code=204)
    mock_api.remove_user_from_repo("myworkspace", "my-repo", "john.doe")

@patch("requests.post")
def test_configure_branch_permissions(mock_post, mock_api):
    mock_post.return_value = Mock(status_code=201, json=lambda: {"branch": "main"})
    response = mock_api.configure_branch_permissions("myworkspace", "my-repo", "main", ["john.doe"])
    assert response == {"branch": "main"}
