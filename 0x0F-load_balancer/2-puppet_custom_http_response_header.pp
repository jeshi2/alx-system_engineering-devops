# 2-puppet_custom_http_response_header.pp

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create a custom HTTP header file
file { '/etc/nginx/custom_headers.conf':
  ensure  => file,
  content => "add_header X-Served-By $hostname;",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Include the custom_headers.conf file in the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('your_module/custom_headers.conf.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Enable the custom header in Nginx configuration
file { '/etc/nginx/sites-available/custom_headers.conf':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Remove the default Nginx default site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    File['/etc/nginx/custom_headers.conf'],
    File['/etc/nginx/sites-available/custom_headers.conf'],
    File['/etc/nginx/sites-enabled/default'],
  ],
}

# Restart Nginx when the custom header or configuration changes
file { '/etc/nginx/custom_headers.conf':
  notify => Service['nginx'],
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/custom_headers.conf':
  notify => Service['nginx'],
  require => Package['nginx'],
}
