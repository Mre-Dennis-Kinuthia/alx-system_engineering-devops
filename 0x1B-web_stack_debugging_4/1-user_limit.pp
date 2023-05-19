# OS configuration so its possible to login with the holberton user and open a file without any error
user { 'holberton':
  ensure => present,
}

file { '/etc/security/limits.conf':
  content => "holberton hard nofile 4096\n",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

exec { 'reload_pam_limits':
  command     => '/usr/sbin/pam-auth-update --package',
  path        => '/usr/sbin',
  refreshonly => true,
}
