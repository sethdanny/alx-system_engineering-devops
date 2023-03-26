# set up my client configuration file using puppet manifest

file_line { 'USE private_key':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
    }
file_line {'TURN OFF Password Auth':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}