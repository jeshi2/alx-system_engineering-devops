# 2-puppet_custom_http_response_header.pp

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create a custom HTTP header file for Nginx
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => file,
  content => "add_header X-Served-By $::hostname;",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    File['/etc/nginx/conf.d/custom_headers.conf'],
  ],
}
