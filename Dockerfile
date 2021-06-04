FROM python:3.9-alpine3.13

RUN apk add --no-cache alpine-sdk tzdata
ENV TZ=America/Sao_Paulo

ENV BROKER \
    BACKEND \
    SAVE_LOG="True"

COPY README.md setup.py /deploy/
COPY producer_consumer_txt /deploy/producer_consumer_txt

VOLUME [ "/deploy", "/deploy/files" ]

WORKDIR /deploy

RUN pip3 install .

EXPOSE 8000
CMD ["gunicorn", "-w", "3", "-b", ":8000", "-k", "uvicorn.workers.UvicornWorker", "-t", "90", "--preload", "--max-requests=500", "producer_consumer_txt:app"]