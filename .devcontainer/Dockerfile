FROM python:3.8.2

ARG USERNAME=color_kurenawi
ARG GROUPNAME=color_kurenawi
ARG USER_UID=1000
ARG USER_GID=1000

COPY requirements.txt /atcoder/
RUN pip install -r /atcoder/requirements.txt

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && groupadd --gid $USER_GID $GROUPNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get -y install sudo \ 
    && echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

ENV PATH /home/$USERNAME/.local/bin:$PATH