#!/usr/bin/env
# This file is used to preprocess the request data before sending it to the
# server.
# It will join every pair of parameter name + parameter value into a single
# query parameter.

# sqlmap -u "http//localhost/index.php?action=foo" --preprocess <path to this file> --dbs --batch

from lib.core.data import logger  # get access to sqlmap logger
from urllib.parse import urlsplit, urlunsplit, urlencode, unquote, quote


def join_parameters(payload):
    """
    Join every pair of parameter name + parameter value into a single query parameter
    """
    # URL decode payload and split by parameter
    payload = unquote(payload)
    parameters = payload.split("&")
    # For each parameter, separate the name and value and join them
    if len(parameters) < 1:
        return payload
    else:
        for i in range(len(parameters)):
            if "=" not in parameters[i]:
                continue
            name, value = parameters[i].split("=", 1)
            parameters[i] = name + "%3D" + quote(value.replace("=", "%3D"))
        # Join all parameters into a single one
        payload = "query=" + "&".join(parameters)
    return payload


def preprocess(req):
    """Join every pair of <parameter name> + <parameter value> into a single "query" parameter"""
    full_url = req.get_full_url()
    # parse the URL
    split_url = urlsplit(full_url)
    query = split_url.query
    query = join_parameters(query)
    full_url = split_url._replace(query=query)
    req.full_url = urlunsplit(full_url)
    logger.debug(f"URL transformed from '{full_url=}' to '{req.full_url}'")
