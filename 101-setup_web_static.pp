# Puppet script to sets up your web servers for the deployment of web_static

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html><head><title>Test Page</title></head><body>Test Content</body></html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Set ownership recursively
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
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
}

# Restart Nginx after updating the configuration
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
