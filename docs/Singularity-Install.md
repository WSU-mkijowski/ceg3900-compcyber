# Singularity 4.3 Build Guide

https://docs.sylabs.io/guides/4.3/user-guide/quick_start.html#quick-installation-steps

Notes include tiny gotchas, like building without `libsubid-dev` and adding Go to `root` `PATH`

Install dependencies
```
$ sudo apt update

$ sudo apt-get install -y \
   autoconf \
   automake \
   cryptsetup \
   fuse2fs \
   git \
   fuse \
   libfuse-dev \
   libseccomp-dev \
   libtool \
   pkg-config \
   runc \
   squashfs-tools \
   squashfs-tools-ng \
   uidmap \
   wget \
   zlib1g-dev \
   build-utils \
   make
# added build-utils and make 
```

Install Go
```
$ export VERSION=1.24.1 OS=linux ARCH=amd64 && \
  wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \
  sudo tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \
  rm go$VERSION.$OS-$ARCH.tar.gz
```

Add Go to PATH for user & root
```
$ echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc && \
  source ~/.bashrc

$ sudo su

# echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc && \
  source ~/.bashrc
```

Download Singularity 4.3
```
$ export VERSION=4.3.0 && \
    wget https://github.com/sylabs/singularity/releases/download/v${VERSION}/singularity-ce-${VERSION}.tar.gz && \
    tar -xzf singularity-ce-${VERSION}.tar.gz && \
    cd singularity-ce-${VERSION}
```

Install Singularity 4.3
```
$ ./mconfig --without-libsubid
$ make -C builddir
$ sudo make -C builddir install
```
