FROM jenkins/jenkins:lts

# Docker CLI yükle (Debian tabanlı Jenkins imajı için)
USER root

RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

USER jenkins
