FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y curl
COPY test.sh .
CMD ["/bin/bash", "test.sh"]
