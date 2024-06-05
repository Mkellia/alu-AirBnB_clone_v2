#!/usr/bin/env bash
# web_static development

# Update and upgrade the system packages
sudo apt-get -y update
sudo apt-get -y upgrade

# Install Nginx if it is not already installed
sudo apt-get -y install nginx

# Create directories for the web_static deployment
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test HTML file
echo "Hello, this is a test HTML file." | sudo tee /data/web_static/releases/test/0-index.html

# Remove any existing symbolic link
sudo rm -rf /data/web_static/current

# Create a new symbolic link to the test release
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart the Nginx service to apply the changes
sudo service nginx restart
