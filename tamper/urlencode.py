#!/usr/bin/env python

import string

from lib.core.enums import PRIORITY
from urllib.parse import quote

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    URL-encodes a given payload (e.g. SELECT FROM -> SELECT%20FROM)

    Notes:
        * May be used as base for more complex encodings

    >>> tamper('SELECT FIELD FROM TABLE')
    'SELECT%20FIELD%20FROM%20TABLE'
    """

    retVal = payload

    if payload:
        retVal = ""
        retVal = quote(payload)

    return retVal
