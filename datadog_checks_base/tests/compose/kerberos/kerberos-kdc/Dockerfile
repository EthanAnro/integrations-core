FROM centos:centos7

# https://github.com/edseymour/kinit-sidecar/blob/master/example-server/Dockerfile

# install kdc and kadmin

# mirrorlist.contos.org does not exits anymore, the below stack exchange post suggests a workaround
# https://serverfault.com/questions/1161816/mirrorlist-centos-org-no-longer-resolve

RUN sed -i s/mirror.centos.org/vault.centos.org/g /etc/yum.repos.d/*.repo && \
    sed -i s/^#.*baseurl=http/baseurl=http/g /etc/yum.repos.d/*.repo && \
    sed -i s/^mirrorlist=http/#mirrorlist=http/g /etc/yum.repos.d/*.repo

RUN yum install -y krb5-server krb5-workstation && yum clean all
RUN mkdir -p /var/kerberos/krb5kdc.d && \
    mkdir -p /etc/krb5.conf.d

ADD init.sh /
ADD kdc.conf /var/kerberos/krb5kdc/
ADD krb5.conf /etc/

RUN chmod g+X,o+X,g+w,a+r -R /var/kerberos && \
    chmod g+X,o+X,g+w,a+r -R /etc/krb5.conf.d && \
    chmod 664 /etc/krb5.conf

RUN sed -i 's|kerberos-adm\ *749/tcp|kerberos-adm\ \ \ \ 8749/tcp|g' /etc/services && \
    sed -i 's|kpasswd\ *464/|kpasswd\ \ \ \ 8464/|g' /etc/services

VOLUME ["/var/kerberos/krb5kdc","/var/kerberos/krb5kdc.d", "/etc/krb5.conf.d" , "/dev/shm" ]
EXPOSE 8888 8464 8749

ENTRYPOINT ["/init.sh"]

