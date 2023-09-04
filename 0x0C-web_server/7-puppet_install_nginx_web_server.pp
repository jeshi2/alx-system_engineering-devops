# Install Nginx web server (w/ Puppet)
exec { 'server configuration':
  provider => shell,
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.html; sudo sed -i "/server_name _;/a location /redirect_me {\n\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default; sudo service nginx restart',
}
