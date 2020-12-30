FROM python:3.8.2

ARG USERNAME=color_kurenawi
ARG GROUPNAME=color_kurenawi
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && groupadd --gid $USER_GID $GROUPNAME \
    && useradd -s /bin/bash --uid $USER_UID $USER_UID \
    && apt-get -y install sudo \ 
    && echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 044 /etc/sudoers.d/$USERNAME

ENV PATH /home/$USERNAME/.local/bin:$PATH