#!/bin/bash

ssl=$(find /etc/ssl -name server.\* | wc -l)

if [ $ssl != 2 ];
then
    echo "GERANDO CERTIFICADO"
    openssl genrsa -out /etc/ssl/server.key 2048
    openssl req -x509 -days 1000 -new -key /etc/ssl/server.key -out /etc/ssl/server.cert --config /etc/ssl/cert.conf
fi
echo "CERTIFICADO PRONTO"