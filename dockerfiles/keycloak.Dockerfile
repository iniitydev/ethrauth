FROM redhat/ubi9 as builder
RUN dnf install -y curl tar --allowerasing
RUN curl -L "https://github.com/Infisical/cli/releases/download/v0.43.23/cli_0.43.23_linux_amd64.tar.gz" -o /tmp/infisical.tar.gz
RUN tar -xvzf /tmp/infisical.tar.gz -C /tmp
RUN mv /tmp/infisical /usr/bin/infisical

FROM quay.io/keycloak/keycloak:24.0
COPY --from=builder /usr/bin/infisical /usr/bin/infisical
