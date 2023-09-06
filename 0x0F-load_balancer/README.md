# Load Balancer and Custom HTTP Header Configuration

This project involves setting up a load balancer and configuring web servers to improve redundancy and handle more traffic. We'll also add a custom HTTP header to track which web server responds to requests. To automate these tasks, we'll use Bash scripts and Puppet manifests.

## Servers
The project involves the following servers:

- `[STUDENT_ID]-web-01` (Ubuntu)
- `[STUDENT_ID]-web-02` (Ubuntu)
- `[STUDENT_ID]-lb-01` (Ubuntu)

## Tasks

### Task 0: Double the Number of Webservers
In this task, we configure `web-02` to be identical to `web-01` and add a custom Nginx response header. The header's name is "X-Served-By," and its value is the hostname of the server running Nginx. We use a Bash script (`0-custom_http_response_header`) to automate this process.

Example usage:
```shell
$ curl -sI 54.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
```

### Task 1: Install Your Load Balancer
In this task, we install and configure HAProxy on `lb-01` to distribute traffic to `web-01` and `web-02` using a round-robin algorithm. We ensure that HAProxy can be managed via an init script. It's essential to have the correct server hostnames ([STUDENT_ID]-web-01 and [STUDENT_ID]-web-02). We use a Bash script to automate this setup.

Example usage:
```shell
$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes
```

### Task 2: Add a Custom HTTP Header with Puppet (Advanced)
In this advanced task, we automate the creation of a custom HTTP header response using Puppet. The header name is "X-Served-By," and the value is the hostname of the server running Nginx. We provide a Puppet manifest (`2-puppet_custom_http_response_header.pp`) to configure a new Ubuntu machine according to the requirements.

---

**Note**: Make sure to replace `[STUDENT_ID]` with your actual student ID or identifier where necessary.
