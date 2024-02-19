#!/usr/bin/env python3

import requests

from lib.core.compat import xrange
from lib.core.enums import PRIORITY

# set these variables for your use case
url = ""
cookies = {}
headers = {}
data = {}

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def getNewToken():
    resp = requests.post(url, headers=headers, cookies=cookies, data=data)
    return resp.json()["access_token"]

def tamper(payload, **kwargs):
    """
    Request new access token based on an active refresh token (need to be set at the script).
    """
    while True:
        try:
            access_token = getNewToken()
            hdrs = kwargs.get("headers", {})
            hdrs["Authorization"] = "Bearer " + access_token
            break
        except:
            pass

    return payload
