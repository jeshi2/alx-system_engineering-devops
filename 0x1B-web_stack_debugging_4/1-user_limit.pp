# 1-user_limit.pp

user { 'holberton':
  ensure => 'present',
}

# Increase open file limit for the user
class { 'limits':
  limits => {
    'holberton' => {
      'hard' => 'unlimited',
      'soft' => 'unlimited',
    },
  },
}
