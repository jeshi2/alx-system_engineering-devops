# Webstack Debugging 0

Welcome to the Webstack Debugging Series! This series is designed to train you in the art of debugging. As a Full-Stack Software Engineer, you'll often find that computers and software don't behave the way you expect, and that's where the "fun" begins.

Debugging a webstack is an essential skill, and it takes practice to become a master at it. In this series, we'll provide you with broken or bugged webstacks, and your goal is to diagnose and fix the issues manually before creating a Bash script that automates the process.

## Getting Started

Let's start with a simple example. Your task is to fix a server that needs two specific elements to function correctly:

1. It should have a copy of the `/etc/passwd` file in the `/tmp` directory.
2. It should have a file named `/tmp/isworking` containing the string "OK".

Without these two elements, the web application cannot work. Your mission is to bring this server to a working state.

## Example Scenario

Here's an example scenario to help you understand the process:

1. Start a Docker container with an Ubuntu 14.04 image:

```bash
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
```

2. Connect to the Docker container:

```bash
vagrant@vagrant:~$ docker exec -ti CONTAINER_ID /bin/bash
```

3. Check the contents of the `/tmp` directory and find that it's empty:

```bash
root@CONTAINER_ID:/# ls /tmp/
```

4. Copy the `/etc/passwd` file to the `/tmp` directory:

```bash
root@CONTAINER_ID:/# cp /etc/passwd /tmp/
```

5. Create a file named `/tmp/isworking` containing the string "OK":

```bash
root@CONTAINER_ID:/# echo OK > /tmp/isworking
```

6. Verify that the `/tmp` directory now contains the required elements:

```bash
root@CONTAINER_ID:/# ls /tmp/
isworking  passwd
```

Your answer file should contain the Bash commands you used to fix the server, as shown in the example above.

## Installing Docker

For this project, you'll be given a container to work with. If you want to experiment locally or on your own VM, you can install Docker on your machine. Here are some resources for installation:

- [Mac OS](https://docs.docker.com/docker-for-mac/install/)
- [Windows](https://docs.docker.com/docker-for-windows/install/)
- [Ubuntu 14.04](https://docs.docker.com/engine/install/ubuntu/)
- [Ubuntu 16.04](https://docs.docker.com/engine/install/ubuntu/)

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the project folder, is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass Shellcheck without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

## Tasks

### Task 0: Give Me a Page!

In this first debugging project, your objective is to get Apache to run on a container and return a page containing "Hello Holberton" when querying the root of the container.

Here's an example scenario to guide you:

1. Start a Docker container with Apache and map port 8080 to port 80:

```bash
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
```

2. Check if the Apache server is running:

```bash
vagrant@vagrant:~$ docker ps
```

3. Use curl to query the container at port 8080:

```bash
vagrant@vagrant:~$ curl 0:8080
```

If it returns "Hello Holberton," you've successfully fixed the issue.
