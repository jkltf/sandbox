#
# Ubuntu 14.04 set JAIST mirror as archive source.
#
FROM ubuntu:14.04

RUN sed -e 's!archive.ubuntu.com!ftp.jaist.ac.jp/pub/Linux!' -i.back /etc/apt/sources.list \
  && apt-get update

