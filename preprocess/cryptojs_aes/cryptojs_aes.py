#!/usr/bin/env
# This preprocess script can be used to encrypt payload using CryptoJS
# JavaScript library. It will use an external JS program.

# sqlmap -u "http//localhost/index.php?action=foo" --preprocess <path to this file> --dbs --batch


import subprocess
from lib.core.data import logger  # get access to sqlmap logger

# ADJUST THESE TO YOUR NEEDS
__ENCRYPTER_PATH = "./src/encrypt_aes.js"
__KEY = "secretkey123"


def preprocess(req):
    """Encrypt original request data using external program and send a JSON
    payload containing the encrypted data in a property called 'data'.
    """
    if req.data:
        command = [
            "node",
            __ENCRYPTER_PATH,
            __KEY,
            req.data,
        ]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        if process.returncode != 0:
            logger.error(
                f"Error while running script ${__ENCRYPTER_PATH}: {error.decode('utf-8')}"
            )
        else:
            data_encrypted = output.decode("utf-8")
            # JSOn payload to be sent
            payload = b'{"data":"' + data_encrypted.strip().encode() + b'"}'
            logger.debug(f"Updated request data: {payload}")
            req.data = payload
