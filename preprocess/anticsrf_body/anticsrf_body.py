#!/usr/bin/env
# This preprocess script will try to find anti-csrf token in a GET response body and set it in the body request data

# sqlmap -u "http//localhost/index.php?action=foo" --preprocess <path to this file> --dbs --batch 

import requests
from bs4 import BeautifulSoup
from lib.core.data import logger # get access to sqlmap logger
from urllib.parse import parse_qs, urlencode

# ADJUST THIS NAME TO YOUR NEEDS
__TOKEN_NAME = b"__RequestVerificationToken"


def getCSRF(html):
    soup = BeautifulSoup(html, 'html.parser')
    csrf = None
    # First, try to find by id
    try:
        csrf = soup.find(id=__TOKEN_NAME).get('value')
    except:
        logger.debug(f"[{__name__}] HTML element with id='{__TOKEN_NAME}' not found")
    else:
        return csrf
    # Try to find by name
    try:
        csrf = soup.find(attrs={"name": __TOKEN_NAME}).get('value')
    except:
        logger.debug(f"[{__name__}] HTML element with attribute name='{__TOKEN_NAME}' not found")
    else:
        return csrf

    return None


def preprocess(req):
    # Request url
    url = req.get_full_url()
    logger.debug(f"[{__name__}] fetching anti-csrf token")

    # Get anti-csrf token from first request
    try:
        r = requests.get(url)
        csrf = getCSRF(r.text)
    except Exception as e:
        logger.debug(f"[{__name__}] {e}]")
    else:
        if csrf is None:
            logger.critical(f"[{__name__}] unable to find requested token")
        else:
            logger.debug(f"[{__name__}] setting {__TOKEN_NAME} to {csrf}")

            # Get original data as a dict
            data = parse_qs(req.data)
            # Set token
            data[__TOKEN_NAME] = csrf
            # Update data
            data = urlencode(data)
            req.data = data.encode('ascii')
