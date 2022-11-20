from github import Github
from typing import List

class GitHubWrapper(object):
    """
    Wrap `PyGithub` for use in Web Projects
    """
    def __init__(self, token: str) -> None:
        self.token = token
        self.github = Github(self.token)

    def repos(self) -> List:
        return self.github.get_user().get_repos()
