# Install the puppet package

package { 'puppet-lint':
  ensure   => 'installed',
  provider => 'gem',
}
