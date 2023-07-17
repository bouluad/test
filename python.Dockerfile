FROM centos:latest

# Install development tools and dependencies
RUN yum -y update && yum -y install \
    gcc \
    make \
    openssl-devel \
    zlib-devel \
    libffi-devel \
    wget \
    tar \
    xz

# Download and install OpenSSL 1.1
WORKDIR /usr/src
RUN wget https://www.openssl.org/source/openssl-1.1.1l.tar.gz && \
    tar -xzvf openssl-1.1.1l.tar.gz && \
    rm openssl-1.1.1l.tar.gz
WORKDIR /usr/src/openssl-1.1.1l
RUN ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl && \
    make && \
    make install

# Update library paths
ENV LD_LIBRARY_PATH=/usr/local/openssl/lib:$LD_LIBRARY_PATH
RUN echo '/usr/local/openssl/lib' >> /etc/ld.so.conf.d/openssl-1.1.1l.conf && ldconfig

# Download and install Python 3.10.1
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/3.10.1/Python-3.10.1.tar.xz && \
    tar -xJf Python-3.10.1.tar.xz && \
    rm Python-3.10.1.tar.xz
WORKDIR /usr/src/Python-3.10.1
RUN ./configure --with-openssl=/usr/local/openssl --enable-optimizations && \
    make && \
    make install

# Verify Python installation
RUN python3 --version

CMD ["bash"]
