FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    xz-utils \
    unzip \
    imagemagick \
    inotify-tools \
    make \
    python3 \
    poppler-utils \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN ARCH=$(dpkg --print-architecture) && \
    if [ "$ARCH" = "arm64" ]; then \
      PANDOC_DEB="pandoc-3.7.0.2-1-arm64.deb"; \
      TYPST_TAR="typst-aarch64-unknown-linux-musl.tar.xz"; \
      TYPST_DIR="typst-aarch64-unknown-linux-musl"; \
    else \
      PANDOC_DEB="pandoc-3.7.0.2-1-amd64.deb"; \
      TYPST_TAR="typst-x86_64-unknown-linux-musl.tar.xz"; \
      TYPST_DIR="typst-x86_64-unknown-linux-musl"; \
    fi && \
    wget -q "https://github.com/jgm/pandoc/releases/download/3.7.0.2/${PANDOC_DEB}" -O /tmp/pandoc.deb && \
    dpkg -i /tmp/pandoc.deb && \
    rm /tmp/pandoc.deb && \
    wget -q "https://github.com/typst/typst/releases/download/v0.15.1/${TYPST_TAR}" -O /tmp/typst.tar.xz && \
    tar -xJf /tmp/typst.tar.xz -C /tmp && \
    mv "/tmp/${TYPST_DIR}/typst" /usr/local/bin/typst && \
    rm -rf /tmp/typst.tar.xz "/tmp/${TYPST_DIR}"

WORKDIR /workspace

CMD ["./build.sh"]