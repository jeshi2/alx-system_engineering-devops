# 1-user_limit.pp

user { 'holberton':
  ensure => 'present',
}

# Set ulimit for the user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => 'present',
  content => "holberton hard nofile unlimited\nholberton soft nofile unlimited\n",
}
