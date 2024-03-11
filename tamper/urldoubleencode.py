#!/usr/bin/env python

import string

from lib.core.enums import PRIORITY
from urllib.parse import quote

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Double URL-encodes a given payload (e.g. SELECT FROM -> SELECT%2520FROM)

    Notes:
        * Useful to payloads that are sent as parameters that becomes URL requests (e.g in a SSRF, RFI attack)

    >>> tamper('SELECT FIELD FROM TABLE')
    'SELECT%2500FIELD%2500FROM%2500TABLE'
    """

    retVal = payload

    if payload:
        retVal = ""
        retVal = quote(quote(payload))

    return retVal
