## VERIFICAR QUAL A MELHOR IMAGEM PARA O PROJETO
# FROM python:3.9-alpine3.13
# FROM python:3.9-slim

# RUN apk add --no-cache alpine-sdk tzdata
ENV TZ=America/Sao_Paulo

COPY ssl /etc/ssl
RUN chmod +x /etc/ssl/gerar_ssl.sh && sh /etc/ssl/gerar_ssl.sh

COPY README.md setup.py /deploy/
COPY producer_consumer_txt /deploy/producer_consumer_txt

VOLUME [ "/deploy" ]

WORKDIR /deploy

RUN pip3 install .

EXPOSE 443
CMD ["gunicorn", "-w", "3", "-b", ":443", "--certfile", "/etc/ssl/server.cert", "--keyfile", "/etc/ssl/server.key", \
     "-k", "uvicorn.workers.UvicornWorker", "-t", "90", "--preload", "--max-requests=500", "producer_consumer_txt:app"]