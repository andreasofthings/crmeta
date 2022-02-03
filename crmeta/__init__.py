

def getSecret(
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

def getService(
    serviceName: str = None,
    serviceVersion: str = None,
    token: str = None,
    secret: str = None,
    client_id: str = None,
    client_secret = None,
    expires: datetime = now
) -> Service:
    from django.utils.timezone import make_naive, is_aware
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    if is_aware(expires_at):
        expires_at = make_naive(expires_at)

    creds = Credentials(
        token=token,
        refresh_token=secret,
        expiry=expires,  # make_aware to default timezone above
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,  # replace with yours
        client_secret=client_secret,
    )
    
    if (service, version) in (("people", "v1", ("gmail", "v1"), ("calendar", "v3")):
        return build("people", version="v1", credentials=creds)
    else:
        raise NotImplementedError
