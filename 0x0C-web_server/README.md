# Web Server Configuration Project

Welcome to the Web Server Configuration project! In this project, you will learn how to configure a web server to meet specific requirements using automation techniques. The project aims to enhance your skills in automating tasks to efficiently manage servers without the need for manual intervention.

## Project Overview

In this project, you will demonstrate your ability to configure a web server (specifically, an Ubuntu machine) according to given requirements. The grading for this project is based on two key aspects:

1. **Server Configuration**: Ensure that your web server, named web-01, is configured as per the specified requirements.
2. **Bash Script**: Create an answer file containing a Bash script that automates the configuration process without any human intervention.

## Why Automation?

The core idea behind this project is to encourage you to automate repetitive tasks. By automating tasks, you can free up your time to focus on more challenging and interesting aspects of your work. For Systems Reliability Engineers (SREs), automation is essential when dealing with a large number of servers. Automation helps maintain consistency, reduce errors, and improve overall efficiency.

## Example Automation Script

Here's an example of what your answer file might look like:

```bash
#!/usr/bin/env bash
# Automated Configuration Script for Web Server (web-01)

# Create a file with a specific content
echo "hello world" > /tmp/test

# Modify Nginx configuration to listen on port 8080
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

Notice that this script automates tasks without requiring manual intervention. The checker will execute your script as the root user, so you don't need to use the `sudo` command.

## Learning Objectives

By completing this project, you will be able to explain the following concepts without relying on external resources:

- The main role of a web server
- The concept of child processes and their importance in web server architecture
- Common HTTP requests and their significance
- The role of DNS (Domain Name System) and its main functions
- Different types of DNS records, including A, CNAME, TXT, and MX

## Resources and References

To successfully complete this project, you can refer to the following resources:

- Understand how the web works
- Learn about Nginx and how to configure it
- Familiarize yourself with the concepts of child processes
- Explore the concept of root and subdomains
- Study different HTTP requests and redirection techniques
- Understand HTTP response codes, including "Not Found" (404)
- Learn about log files on Linux and their significance

You can also refer to the following references:

- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)
- Utilize `man` or `help` commands for `scp` and `curl` to deepen your understanding of these tools.

## Testing Your Automation Script

Feel free to test your Bash script in a controlled environment. You can:

1. Start a Ubuntu 16.04 sandbox.
2. Run your script on the sandbox.
3. Observe how the script behaves and whether it meets the requirements.

Remember, a good software engineer embraces automation to streamline their work, improve efficiency, and eliminate manual errors. Happy automating!

Remember the mantra: A good Software Engineer is a lazy Software Engineer. 🚀
