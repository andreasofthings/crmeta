

def getSecrets(
    projectName: str = None,
    secretName: str = None,
    version: str = "latest"
) -> dict:
    import json
    from google.cloud import secretmanager

    secrets = secretmanager.SecretManagerServiceClient()
    name = f"projects/{projectName}/secrets/{secretName}/versions/{version}"
    response = secrets.access_secret_version(
        request={"name": name})
    secret = json.loads(response.payload.data.decode('UTF-8'))
    return secret
