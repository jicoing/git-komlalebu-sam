FROM python:3.8-alpine

ENV AWSCLI_VERSION='1.5.2'

RUN pip install --quiet --no-cache-dir awscliv2==${AWSCLI_VERSION}


COPY entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]