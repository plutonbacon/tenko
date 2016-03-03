# Base image
FROM debian:jessie

ENV MYSQL_MAJOR 5.7
ENV MYSQL_VERSION 5.7.11-1debian8

# Add a dedicated user and group first to make sure their IDs are assigned consistently, regardless
# of whatever dependencies are added later
RUN groupadd -r mysql && useradd -r -g mysql mysql

# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5

RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list

RUN { \
		echo mysql-community-server mysql-community-server/data-dir select ''; \
		echo mysql-community-server mysql-community-server/root-pass password ''; \
		echo mysql-community-server mysql-community-server/re-root-pass password ''; \
		echo mysql-community-server mysql-community-server/remove-test-db select false; \
	} | debconf-set-selections

# Packaged dependencies
RUN apt-get update && apt-get install -y \
    mysql-server="${MYSQL_VERSION}" \
    perl \
    pwgen \
    --no-install-recommends \
    rm -rf /var/lib/mysql \
    mkdir -p /var/lib/mysql \
    rm -rf /var/lib/apt/lists/*

RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \
	&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \
	&& mv /tmp/my.cnf /etc/mysql/my.cnf

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld"]