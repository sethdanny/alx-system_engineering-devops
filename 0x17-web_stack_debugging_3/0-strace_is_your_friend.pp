# fix file extension typo in the php file
exec { 'replace phpp with php':
  command  => 'sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php',
  provider => shell
}

#restart apache2 service
exec { 'restart apache2 service':
  command  => 'service apache2 restart',
  provider => shell
}
