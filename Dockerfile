FROM jenkins/jenkins:lts

USER root

# Docker CLI yükle
RUN apt-get update && apt-get install -y docker.io

USER jenkins
