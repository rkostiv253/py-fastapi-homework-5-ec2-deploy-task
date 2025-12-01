FROM debian:bookworm-slim

# Install tools needed to download MailHog and prepare the script
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Download the prebuilt MailHog binary and make it executable
RUN wget -O /usr/local/bin/MailHog \
      https://github.com/mailhog/MailHog/releases/download/v1.0.1/MailHog_linux_amd64 \
    && chmod +x /usr/local/bin/MailHog

# Copy your auth setup script into the image
COPY commands/setup_mailhog_auth.sh /commands/setup_mailhog_auth.sh

# Normalize line endings and make the script executable
RUN dos2unix /commands/setup_mailhog_auth.sh && chmod +x /commands/setup_mailhog_auth.sh

# Default command: configure auth and start MailHog
CMD ["/bin/bash", "-c", "/commands/setup_mailhog_auth.sh && MailHog"]
