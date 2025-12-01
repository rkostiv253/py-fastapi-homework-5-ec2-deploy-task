# Use official Go 1.22 image based on Debian Bookworm
FROM golang:1.22-bookworm

# Install tools for script + certificates
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    dos2unix \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install MailHog using Go (now Go 1.22, so deps compile)
RUN go install github.com/mailhog/MailHog@latest

# MailHog binary lands in /go/bin
ENV PATH="/go/bin:${PATH}"

# Copy your auth setup script
COPY commands/setup_mailhog_auth.sh /commands/setup_mailhog_auth.sh

# Fix line endings and make it executable
RUN dos2unix /commands/setup_mailhog_auth.sh && chmod +x /commands/setup_mailhog_auth.sh

# Default command: run your script, then start MailHog
CMD ["/bin/bash", "-c", "/commands/setup_mailhog_auth.sh && MailHog"]
