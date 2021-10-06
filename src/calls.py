#! /usr/bin/env
import webbrowser
import esipy
from esipy import EsiClient
from esipy import EsiSecurity
from esipy.utils import generate_code_verifier

version = "0.0.1"
full_version = "EVEterm 0.0.1 Pre-Alpha"
long_version = "EVEterm 0.0.1 Pre-Alpha \"Buggy testing hellscape\""


def auth():
    # creating the security object using the app
    security = EsiSecurity(
        headers={'User-Agent': full_version},
        redirect_uri='http://localhost/callback',
        client_id='a2c6fb5fa9a3400b81eef46ea8b9c980',
        code_verifier=generate_code_verifier(),
    )

    client = EsiClient(security=security,
                       headers={'User-Agent': full_version}, )

    # this will give you the url where your user must be redirected to.
    eve_sso_auth_url = security.get_auth_uri(
        state="Do I really need this",
        scopes=['esi-skills.read_skills.v1', 'esi-skills.read_skillqueue.v1']
        # or None (default) if you don't need any scope
    )
    print(eve_sso_auth_url)
    webbrowser.open_new_tab(eve_sso_auth_url)

    code_param = input("Enter the code parameter here")
    tokens = EsiSecurity().auth(redirect_uri=eve_sso_auth_url, client_id='a2c6fb5fa9a3400b81eef46ea8b9c980')
    print(tokens)

    # tokens is actually a json objects with these values:
    # {
    #     "access_token":"uNEEh...a_WpiaA2",
    #     "token_type":"Bearer",
    #     "expires_in":1200,
    #     "refresh_token":"gEy...fM0"
    # }
    EsiSecurity().verify()
    # This gives you some JSON object with a lot of info
