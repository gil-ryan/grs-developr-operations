# Setting up a LAMP environment

## Linux

Validate your OS is appropriate, meaning, it is a linux box. Once you're all setup, you may proceed with updating the OS to its most recent version with the CLI.

> sudo apt-get update

## Apache

> sudo apt-get install apache2
> sudo service apache2 status

### Test Apache

> sudo service apache2 status

If everything installed correctly, you will receive this output:
Apache is active and running in Ubuntu.
3. Next, make sure that the UFW firewall has an application profile for Apache by typing in the following command:
sudo ufw app list
In the Apache Full profile, make sure it allows the traffic on ports 80 and 443. Check this by typing the command:
sudo ufw app info “Apache Full”

## MySQL

> sudo apt-get install mysql-server

## PhP

> sudo apt-get install php libapache2-mod-php php-mysql
