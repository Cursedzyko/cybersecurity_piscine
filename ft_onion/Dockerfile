# Use a base image with Ubuntu
FROM ubuntu:20.04

# Update package list and install required packages
RUN apt-get update && apt-get install -y \
    nginx \
    openssh-server \
    tor \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up SSH
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/Port 22/Port 4242/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Copy configuration files
COPY nginx.conf /etc/nginx/nginx.conf
COPY sshd_config /etc/ssh/sshd_config
COPY torrc /etc/tor/torrc
COPY index.html /var/www/html/index.html

# Set permissions for the web directory
RUN chmod -R 755 /var/www/html

# Expose required ports
EXPOSE 4242 80

# Start the services: nginx, ssh, and tor
CMD ["sh", "-c", "service nginx start && service ssh start && tor"]
