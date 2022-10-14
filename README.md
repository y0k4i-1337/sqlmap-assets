# sqlmap-assets
Customizations for sqlmap

## Preprocess script

In order to use one or more comma-separated pre-process scripts, save the folder of desired script in your machine and
use sqlmap option `--preprocess`. This option expect the path for the pre-process scripts that are to be used.

Example:

```bash
sqlmap.py -r request.txt --preprocess ./anticsrf_body/anticsrf_body.py
```

## Tamper script

In order to use custom tamper scripts, just copy them to directory `${SQLMAP_DIR}/tamper` and invoke them as usual.
