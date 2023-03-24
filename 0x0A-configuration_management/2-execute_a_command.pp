# create a puppet mainfest file to kill a running process called killmenow
exec{ 'pkill':
    command  => 'pkill -f killmenow',
    provider => 'shell',
    }
