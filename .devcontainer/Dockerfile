FROM python:3.8.2

ARG USERNAME=color_kurenawi
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

ENV DEBIAN_FRONTEND noninteractive

# user add and as add the user to sudoers
RUN apt-get update \
    && groupadd --gid ${USER_GID} ${GROUPNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && apt-get -y install sudo \ 
    && echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

# pypy3 installation
RUN wget -P /tmp/ https://downloads.python.org/pypy/pypy3.6-v7.3.3-linux64.tar.bz2 \
    && tar -xf /tmp/pypy3.6-v7.3.3-linux64.tar.bz2 -C /opt/ \
    && ln -s /opt/pypy3.6-v7.3.3-linux64/bin/pypy3  /usr/local/bin/pypy3

# Python third party library installation
COPY requirements.txt /tmp/
RUN python -m pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

# oj-tools setup
RUN apt-get update \
    && apt-get install -y time
USER ${USERNAME}
COPY oj-setup.sh /tmp
RUN bash /tmp/oj-setup.sh

ENV DEBIAN_FRONTEND newt