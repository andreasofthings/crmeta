from github import Github
from typing import List
from django.contrib.auth import get_user_model

User = get_user_model()

class GitHubWrapper(object):
    """
    Wrap `PyGithub` for use in Web Projects
    """
    def __init__(self, token: str) -> None:
        self.token = token
        self.github = Github(self.token)

    def repos(self) -> List:
        return self.github.get_user().get_repos()
