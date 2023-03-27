# Create a manifest that kills a process named killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
}
