
# this is c5xb

## docker 

This document describes the use of Docker within the c5xb project. 

FROM ghcr.io/sigboe/gnome-shell-docker:master

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    gjs \
    gnome-shell-extensions \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Set up workspace
WORKDIR /workspace

# Copy extension files
COPY . .

# Test environment setup
ENV DISPLAY=:0
ENV MUTTER_DEBUG_DUMMY_MODE_SPECS=1024x768

# Command to run when container starts
CMD ["gnome-shell", "--nested", "--wayland"]
