FROM python:3.8.2

ARG USERNAME=color_kurenawi
ARG GROUPNAME=color_kurenawi
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && groupadd --gid ${USER_GID} ${GROUPNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && apt-get -y install sudo \ 
    && echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

RUN wget -P /tmp/ https://downloads.python.org/pypy/pypy3.7-v7.3.3-linux64.tar.bz2 \
    && tar -xf /tmp/pypy3.7-v7.3.3-linux64.tar.bz2 -C /opt/ \
    && ln -s /opt/pypy3.7-v7.3.3-linux64/bin/pypy3  /usr/local/bin/pypy3

COPY requirements.txt /atcoder/
RUN python -m pip install --upgrade pip \
    && pip install -r /atcoder/requirements.txt

RUN apt-get update \
    && wget -P /tmp/ https://deb.nodesource.com/setup_12.x \
    && bash /tmp/setup_12.x \
    && apt-get install -y build-essential nodejs\
    && npm install -g atcoder-cli

USER ${USERNAME}
COPY atcoder-cli-config.sh  /tmp
RUN sh /tmp/atcoder-cli-config.sh

ENV DEBIAN_FRONTEND newt