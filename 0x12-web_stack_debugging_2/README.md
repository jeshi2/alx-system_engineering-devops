# Webstack02 Nginx Configuration Script

This Bash script is designed to configure an Nginx web server to run as the `nginx` user and listen on port 8080. It also ensures that any running Apache2 processes are terminated before starting Nginx.

## Usage

1. Ensure you have the necessary permissions to modify Nginx configuration files and restart the service. You may need superuser (root) privileges.

2. Download or create the Bash script

3. Make the script executable:

```bash
chmod +x configure_nginx.sh
```

4. Run the script to configure Nginx:

```bash
./configure_nginx.sh
```

## Explanation

- The script uses the `sed` command to edit the Nginx configuration files:
  - `sed -i 's/#user www-data/user nginx/' /etc/nginx/nginx.conf` replaces the comment `#user www-data` with `user nginx` in the `nginx.conf` file, changing the user under which Nginx runs to `nginx`.
  - `sed -i 's/80/8080/g' /etc/nginx/sites-available/default` replaces port `80` with `8080` in the default site configuration, changing the default listening port to `8080`.
  - `chmod 644 /etc/nginx/nginx.conf` ensures the modified `nginx.conf` file has the correct permissions.

- `pkill apache2` terminates any running Apache2 processes. This step is optional and may not be needed in all cases. It's included to ensure that Apache2 doesn't interfere with Nginx.

- Finally, `service nginx start` restarts the Nginx service with the new configuration.

Please note that you should review and adapt this script to your specific server setup and requirements. Ensure you have backups and test the script in a safe environment before applying it to a production server.

---
