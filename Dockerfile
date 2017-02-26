FROM python:2.7
MAINTAINER Eric Horne <eric.horne@box11.org>

VOLUME /home/scheds
WORKDIR /home/scheds

RUN pip install lxml requests &&\
    git config --global user.email "cvpsp@box11.org" &&\
    git config --global user.name "Conejo Valley PONY Schedule Puller"

CMD ["./pullscheds"]
