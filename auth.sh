#! /bin/bash
secret='POJONYMZE45SK3MH2QEXMEO6HQ'

while :
do
	totp=$(oathtool --totp $secret -b)
	echo $totp
	line="api.generateSession('P892158', '5542', '$totp')"
	sed -i  -e "6s/.*/$line/g" app.py
	sleep 30
done
