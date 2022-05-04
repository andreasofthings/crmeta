from django.contrib.auth import get_user_model

def getSecret(
    projectName: str = None, secretName: str = None, version: str = "latest"
) -> dict:
    import json
    from google.cloud import secretmanager

    secrets = secretmanager.SecretManagerServiceClient()
    name = f"projects/{projectName}/secrets/{secretName}/versions/{version}"
    response = secrets.access_secret_version(request={"name": name})
    secret = json.loads(response.payload.data.decode("UTF-8"))
    return secret

User = get_user_model()
def getGoogleService(
    user: User,
    provider: str = "Google",
    providerNumber: int = 0,
    accountNumber: int = 0
) -> str:
    """
    provider: Defaults to Google
    providerNumber: could be connected to multiple Providers, index to further
    accountNumber: optional, index to further accounts than the first available

    raises::
        NotFoundException if no account is found.
    """
    from allauth.socialaccount.models import SocialToken, SocialApp
    from google.oauth2.credentials import Credentials
    from django.utils.timezone import make_naive, is_aware
    from googleapiclient.discovery import build

    access_token = SocialToken.objects.filter(  # pylint: disable=no-member
        account__user=self.request.user, account__provider="google"
    )[accountNumber]
    app = SocialApp.objects.filter(provider=provider)[providerNumber]

    expires_at = access_token.expires_at
    if is_aware(access_token.expires_at):
        """
            .. todo:
            this is a hack. it converts `expires_at` to the default
            timezone set in `settings.py` for the project.
            However, it should rather use the timezone in which Google
            issued this token. This **MAY** be contained in `access_token`.
            Actually, it seems to be the other way round...
        """
        expires_at = make_naive(access_token.expires_at)

    creds = Credentials(
        token=access_token.token,
        refresh_token=access_token.token_secret,
        expiry=expires_at,  # make_aware to default timezone above
        token_uri="https://oauth2.googleapis.com/token",
        client_id=app.client_id,
        client_secret=app.secret,
    )

    service = build("people", version="v1", credentials=creds)
    return service
