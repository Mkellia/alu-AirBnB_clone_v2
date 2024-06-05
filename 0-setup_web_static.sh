#!/usr/bin/env bash
# web_static development

# Update and upgrade the system packages
sudo apt-get -y update
sudo apt-get -y upgrade

# Install Nginx if it is not already installed
sudo apt-get -y install nginx

# Create directories for the web_static deployment
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create the HTML file with the specified content
cat <<EOF | sudo tee /data/web_static/releases/test/index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">Holberton School</p>
        </footer>
    </body>
</html>
EOF

# Remove any existing symbolic link
sudo rm -rf /data/web_static/current

# Create a new symbolic link to the test release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}' /etc/nginx/sites-available/default

# Restart the Nginx service to apply the changes
sudo service nginx restart
