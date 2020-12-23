#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo chmod 666 /var/www/html/index.nginx-debian.html
mkdir -p data/{web_static/{releases/test/,shared}}
echo "<html>
          <head></head>
          <body>Hello, Holberton</body>
      </html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data/
sudo sed -i 's/location / {/a location /hbnb_static { alias /data/web_static/current/hbnb_static/;/'  /etc/nginx/sites-available/default
sudo service nginx restart


