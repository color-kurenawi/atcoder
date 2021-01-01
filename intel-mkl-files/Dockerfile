FROM python:3.8.2

ARG USERNAME=color_kurenawi
ARG GROUPNAME=color_kurenawi
ARG USER_UID=1000
ARG USER_GID=1000

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && groupadd --gid $USER_GID $GROUPNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get -y install sudo \ 
    && echo $USERNAME ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

COPY .numpy-site.cfg /root
COPY intel-mkl-setup.sh /tmp
RUN sh tmp/intel-mkl-setup.sh

RUN apt-get update \
    && apt-get install -y intel-mkl-2020.0-088 gfortran \
    && python -m pip config set install.no-binary "numpy,scipy" \
    && python -m pip config set wheel.no-binary "numpy,scipy"

ENV MKL_ROOT_DIR $MKL_ROOT_DIR:/opt/intel/mkl
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$MKL_ROOT_DIR/lib/intel64:/opt/intel/lib/intel64_lin
ENV LIBRARY_PATH $LIBRARY_PATH:$MKL_ROOT_DIR/lib/intel64

COPY requirements.txt /atcoder/
RUN pip install -r /atcoder/requirements.txt

RUN apt-get update \
    && apt-get install -y nodejs npm \
    && npm install -g atcoder-cli

USER $USERNAME
COPY atcoder-cli-config.sh  /tmp
RUN sh /tmp/atcoder-cli-config.sh


ENV PATH /home/$USERNAME/.local/bin:$PATH