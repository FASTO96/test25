FROM php:8.2-apache

# Copy PHP file to Apache root
COPY main.php /var/www/html/main.php

# Copy version.txt and lg.txt
COPY version.txt /var/www/html/version.txt
COPY lg.txt /var/www/html/lg.txt
