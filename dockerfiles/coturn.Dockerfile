FROM coturn/coturn:latest

USER root

RUN apt-get update && apt-get install -y curl
RUN curl -1sLf \
'https://dl.cloudsmith.io/public/infisical/infisical-cli/setup.deb.sh' \
| bash

RUN apt-get install -y infisical

USER coturn
