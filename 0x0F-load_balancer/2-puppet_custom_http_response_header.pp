# Define a class to configure the custom HTTP header
class custom_http_response_header {

  # Install Nginx
  package { 'nginx':
    ensure => installed,
  }

  # Define a custom Nginx configuration file
  file { '/etc/nginx/sites-available/custom-header':
    ensure  => present,
    content => "server {
        listen 80;
        server_name _;
        add_header X-Served-By $hostname;
        location / {
            proxy_pass http://localhost:8080;
        }
    }",
    require => Package['nginx'],
  }

  # Create a symbolic link to enable the custom site
  file { '/etc/nginx/sites-enabled/custom-header':
    ensure => link,
    target => '/etc/nginx/sites-available/custom-header',
    require => File['/etc/nginx/sites-available/custom-header'],
  }

  # Remove the default Nginx site
  file { '/etc/nginx/sites-enabled/default':
    ensure => absent,
    notify => Service['nginx'],
  }

  # Test Nginx configuration and reload Nginx
  exec { 'nginx-config-test':
    command => 'nginx -t',
    path    => '/usr/sbin:/usr/bin:/sbin:/bin',
    notify  => Service['nginx'],
  }
}

# Apply the custom HTTP header class
include custom_http_response_header

