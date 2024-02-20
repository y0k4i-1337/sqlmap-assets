# Instructions

Simply replace `__ENCRYPTER_PATH` at
[cryptojs_aes.py](cryptojs_aes.py#L12) with the path of program used to encrypt the
payload and `__KEY` at [cryptojs_aes.py](cryptojs_aes.py#L13) with the key used to
encrypt data.

## Example of use case

### Preconditions

1. Your target encrypt data sent to server using `CryptoJS`.
1. You have acquired the key and any other parameters used by `CryptoJS`.

### Common workflow

1. Decrypt a previous captured request using [decrypt_aes.js](src/decrypt_aes.js).
1. In the request file that will be used by `sqlmap`, replace encrypted data by
   its decrypted version.
1. Mark the injection points using `*` or `-p` option when calling `sqlmap`.
1. Make proper modifications at [cryptojs_aes.py](cryptojs_aes.py) to fit your
   needs, including the variables described above and the format of final
   payload at [this line](cryptojs_aes.py#L38).
1. Have some :coffee: while `sqlmap` do its job!
