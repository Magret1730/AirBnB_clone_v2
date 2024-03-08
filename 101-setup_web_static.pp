# Puppet script to sets up your web servers for the deployment of web_static

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Running nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Set ownership recursively
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}",
  require => Package['nginx'],
  notify  => Exec['nginx-reload'],
}

# Restart Nginx after updating the configuration
exec { 'nginx-reload':
  command     => 'sudo service nginx restart',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
