# kill process killmenow that run on the machine
exec {'killmenow':
command => 'pkill killmenow',
path    => '/usr/bin:/usr/sbin:/bin',
}
