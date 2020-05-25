#/usr/bin bash

curl 'https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeral' \
    -H 'Accept: application/json, text/plain, */*' \
    -H 'Accept-Language: en-GB,en;q=0.5' \
    --compressed -H 'X-Parse-Application-Id: unAFkcaNDeXajurGB7LChj8SgQYS2ptm' \
    -H 'Origin: https://covid.saude.gov.br' -H 'Connection: keep-alive' \
    -H 'Referer: https://covid.saude.gov.br/' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' \
    -H 'TE: Trailers' | python3 -c "import sys, json; print(json.load(sys.stdin)['results'][0]['arquivo']['url'])"
