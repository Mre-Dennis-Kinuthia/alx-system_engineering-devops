# OS configuration so its possible to login with the holberton user and open a file without any error
exec { 'change-os-configuration-for-holberton-user':
command  => "sed -i 's/4096/16384/' /etc/security/limits.conf",
provider => 'shell',
}
