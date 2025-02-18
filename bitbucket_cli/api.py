import requests
from requests.auth import HTTPBasicAuth
from .config import Config

class BitbucketAPI:
    def __init__(self):
        self.auth = HTTPBasicAuth(Config.BITBUCKET_USERNAME, Config.BITBUCKET_ACCESS_TOKEN)

    def create_project(self, workspace, project_name, project_key):
        url = f"{Config.BITBUCKET_API_URL}/workspaces/{workspace}/projects/"
        data = {
            "name": project_name,
            "key": project_key,
            "is_private": True
        }
        response = requests.post(url, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def create_repo(self, workspace, project_key, repo_name):
        url = f"{Config.BITBUCKET_API_URL}/repositories/{workspace}/{repo_name}"
        data = {
            "scm": "git",
            "project": {"key": project_key},
            "is_private": True
        }
        response = requests.post(url, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def add_user_to_repo(self, workspace, repo_slug, username, permission):
        url = f"{Config.BITBUCKET_API_URL}/repositories/{workspace}/{repo_slug}/permissions-config/users/{username}"
        data = {
            "permission": permission
        }
        response = requests.put(url, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def remove_user_from_repo(self, workspace, repo_slug, username):
        url = f"{Config.BITBUCKET_API_URL}/repositories/{workspace}/{repo_slug}/permissions-config/users/{username}"
        response = requests.delete(url, auth=self.auth)
        response.raise_for_status()

    def configure_branch_permissions(self, workspace, repo_slug, branch_name, exempt_users):
        url = f"{Config.BITBUCKET_API_URL}/repositories/{workspace}/{repo_slug}/branch-restrictions"
        data = {
            "kind": "require_pull_request_to_merge",
            "pattern": branch_name,
            "users": [{"username": user} for user in exempt_users]
        }
        response = requests.post(url, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()
