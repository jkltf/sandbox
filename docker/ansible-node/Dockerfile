FROM myubuntu:14.04_jaist

RUN apt-get update \
  && apt-get install -y python python-setuptools
RUN apt-get install -y ssh \
  && mkdir -p /var/run/sshd

RUN easy_install supervisor
ADD supervisord.conf /etc/

RUN useradd -m ansiblenode \
  && mkdir -p /home/ansiblenode/.ssh \
  && chmod 700 /home/ansiblenode/.ssh \
  && chown ansiblenode:ansiblenode -R /home/ansiblenode
ADD id_rsa-ansible_host.pub /home/ansiblenode/.ssh/authorized_keys
RUN chmod 400 /home/ansiblenode/.ssh/authorized_keys \
  && chown ansiblenode:ansiblenode /home/ansiblenode/.ssh/authorized_keys
ADD sudores.d.ansiblenode /etc/sudoers.d/ansiblenode

RUN locale-gen en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

EXPOSE 22
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]

