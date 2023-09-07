# HTTPS SSL

This README provides instructions and details for completing two tasks related to configuring and securing web services using HAproxy and SSL termination. These tasks are part of a larger project and have specific requirements.

## Task 0: World Wide Web

### Objective
Configure your domain zone to point various subdomains to specific IP addresses and create a Bash script to display information about these subdomains.

### Requirements
1. Add the following subdomains to your domain:
   - www (point it to your lb-01 IP)
   - lb-01 (point it to your lb-01 IP)
   - web-01 (point it to your web-01 IP)
   - web-02 (point it to your web-02 IP)
   
2. Create a Bash script that accepts two arguments:
   - `domain`: The domain name to audit (mandatory)
   - `subdomain`: The specific subdomain to audit (optional)

3. The script should display information in the format:
   ```
   The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
   ```

4. If only the `domain` parameter is provided, display information for its subdomains in the following order: www, lb-01, web-01, and web-02.

5. When passing both `domain` and `subdomain` parameters, display information for the specified subdomain.

6. Ignore ShellCheck case SC2086.

7. Use `awk` and at least one Bash function.

### Example
```bash
$ ./0-world_wide_web holberton.online
The subdomain www is an A record and points to 54.210.47.110
The subdomain lb-01 is an A record and points to 54.210.47.110
The subdomain web-01 is an A record and points to 34.198.248.145
The subdomain web-02 is an A record and points to 54.89.38.100

$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is an A record and points to 54.89.38.100
```

## Task 1: HAproxy SSL Termination

### Objective
Configure HAproxy to handle encrypted traffic and terminate SSL for the subdomain www.

### Requirements
1. HAproxy should listen on port TCP 443.

2. HAproxy should be configured to accept SSL traffic.

3. HAproxy should serve encrypted traffic that returns the root ("/") of your web server.

4. When querying the root of your domain name, the page returned must contain "Holberton School."

5. Share your HAproxy configuration as an answer file located at `/etc/haproxy/haproxy.cfg`.

6. Make sure to install HAproxy 1.5 or higher, as SSL termination is not available in versions before v1.5.

### Example
```bash
$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

$ curl https://www.holberton.online
Holberton School for the win!
```

## Notes
Please ensure that you follow the requirements and examples closely to successfully complete these tasks.
