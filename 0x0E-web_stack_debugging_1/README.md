# Web stack debugging #1


# Task 0: Nginx likes port 80

## Introduction
This README explains Task 0, which involves debugging and fixing an issue with an Nginx installation in an Ubuntu container that prevents it from listening on port 80. You will need to find and fix the issue, and then create a Bash script to automate the fix.

## Task Description
- **Mandatory:** Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue.
- **Mandatory:** Write a Bash script with the minimum number of commands to automate your fix.
- **Requirements:** 
  - Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs.
  
### Debugging Process
1. Access the Ubuntu container where Nginx is installed.
2. Use debugging tools to identify the issue preventing Nginx from listening on port 80.
3. Install any necessary tools to aid in debugging.
4. Start and stop containers as needed to test your solutions.

### Bash Script
- Create a Bash script that configures the server to meet the above requirements.

### Testing
- Test the script to ensure it successfully resolves the issue.
- Verify that Nginx is running and listening on port 80.

## Usage
To run the script, use the following command:
```
./0-nginx_likes_port_80
```

## Example Output
After running the script, you should see the following output:
```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

# Task 1: Make it sweet and short

## Introduction
This README explains Task 1, which builds upon Task 0. In this task, you are required to make your Bash script even shorter and more concise.

## Task Description
- **Advanced:** Based on your solution from Task 0, create a Bash script that is 5 lines long or less.
- **Requirements:** 
  - The script must be extremely concise (5 lines or less).
  - There must be a new line at the end of the file.
  - You must respect usual Bash script requirements.
  - You cannot use `;`.
  - You cannot use `&&`.
  - You cannot use `wget`.
  - You cannot execute your previous answer file (Do not include the name of the previous script in this one).
  - The `service` (init) must report that Nginx is not running (for real).

## Usage
To run the concise Bash script, use the following command:
```
./1-debugging_made_short
```

## Example Output
After running the concise script, you should see the following output:
```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

After running the script, the `service nginx status` command should report that Nginx is not running:
```
* nginx is not running
```
