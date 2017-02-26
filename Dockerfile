FROM python:2.7
MAINTAINER Eric Horne <eric.horne@box11.org>

VOLUME /home/scheds
WORKDIR /home/scheds

RUN pip install lxml requests

CMD ["./pullscheds"]
