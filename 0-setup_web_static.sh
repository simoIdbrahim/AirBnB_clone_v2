#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null;
then
sudo apt-get update
sudo apt-get -y install nginx
sudo service nginx start
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

sudo sh -c 'echo "Hello World!" > /data/web_static/releases/test/index.html'

source_path="/data/web_static/releases/test/"
symlink_path="/data/web_static/current"
if [ -h "$symlink_path" ]; then
    rm "$symlink_path"
fi

sudo ln -s "$source_path" "$symlink_path"

sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu /data/

df_path="/etc/nginx/sites-available/default"
new_loc="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/^\tserver_name _;/a\\$new_loc" $df_path
sudo service nginx restart
