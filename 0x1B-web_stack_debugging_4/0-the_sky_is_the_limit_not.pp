# 0-the_sky_is_the_limit_not.pp

# Ensure Nginx is installed
class { 'nginx':
  ensure => 'installed',
}

# Define a virtual host for your web application
nginx::resource::vhost { 'my_website':
  ensure     => present,
  listen_ip  => '0.0.0.0',
  listen_port => '80',
  server_name => 'localhost',
  location   => {
    '/' => {
      proxy => 'http://127.0.0.1:8080', # Change the proxy as needed
    },
  },
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Nginx::Resource::Vhost['my_website'],
}
