# wp-settings
exec {'modify file':
command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
path    => '/bin/',
}
