import json
from google.cloud import secretmanager


def getSecret(
    projectName: str = None, secretName: str = None, version: str = "latest"
) -> dict:
    """
    projectName: name of the project
    secretName: name of the secret
    version: version of the secret, defaults to 'latest'

    .. 
    """
    secrets = secretmanager.SecretManagerServiceClient()
    name = f"projects/{projectName}/secrets/{secretName}/versions/{version}"
    response = secrets.access_secret_version(request={"name": name})
    secret = json.loads(response.payload.data.decode("UTF-8"))
    return secret
