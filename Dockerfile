FROM python:alpine

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.32.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.32.0/allure-commandline-2.32.0.tgz && \
    tar -zxvf allure-2.32.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.32.0/bin/allure /usr/bin/allure && \
    rm allure-2.32.0.tgz

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install -r requirements.txt