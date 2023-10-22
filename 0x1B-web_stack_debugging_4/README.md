# Web Stack Debugging #4

This repository contains solutions to web stack debugging tasks. The tasks are designed to help you identify and resolve issues in a web server setup using Nginx.

## Table of Contents

- [Task 1: Identify and Fix High Open File Limit](#task-1-identify-and-fix-high-open-file-limit)
- [Task 2: Additional Tasks (List them as needed)](#task-2-additional-tasks-list-them-as-needed)

# Task 0: Sky is the Limit, Let's Bring That Limit Higher

In this web stack debugging task, you will learn how to improve the performance of a web server setup featuring Nginx. The goal is to reduce the number of failed requests and optimize the server's response.

## Problem Description

You have observed that the web server setup, featuring Nginx, is not performing well under pressure. When benchmarking with ApacheBench, a significant number of requests are failing, resulting in a suboptimal user experience.

Benchmarking results before debugging:

- Total requests: 2000
- Failed requests: 943
- Server Software: Nginx/1.4.6

## Debugging and Solution

### Task Overview

- Analyze the benchmarking results to identify the specific issues affecting server performance.
- Develop a Puppet manifest (0-the_sky_is_the_limit_not.pp) to address the identified issues and improve server performance.
- Apply the Puppet manifest to make the necessary changes.

### Key Improvements

- Detailed analysis of ApacheBench results to understand the problems.
- The use of Puppet to automate server configuration changes.
- Improving the server's ability to handle concurrent requests.

## Benchmarking Results After Debugging

After applying the Puppet manifest (0-the_sky_is_the_limit_not.pp), the benchmarking results have improved significantly:

- Total requests: 2000
- Failed requests: 0
- Server Software: Nginx/1.4.6

## How to Apply the Solution

1. Ensure that you have Puppet installed on your system. If not, install it using your system's package manager.

2. Copy the `0-the_sky_is_the_limit_not.pp` Puppet manifest to your server.

3. Apply the Puppet manifest to make the necessary configuration changes:

```bash
puppet apply 0-the_sky_is_the_limit_not.pp
```

## Task 1: Identify and Fix High Open File Limit

In this task, we encountered issues when trying to log in as the "holberton" user, where we received "Too many open files" errors. The objective was to change the OS configuration so that it's possible to log in as the "holberton" user and open files without any error message.

**Solution**:

- We created a Puppet manifest (`1-user_limit.pp`) to increase the open file limit for the "holberton" user.
- The manifest ensures the "holberton" user exists on the system and sets the open file limit to "unlimited" for both soft and hard limits.

To apply the solution:

```bash
puppet apply 1-user_limit.pp
```


## Conclusion

These tasks are designed to help you learn and practice web stack debugging. Feel free to explore additional tasks and challenges to enhance your debugging skills.

**Note**: Ensure that you have the necessary permissions and backups before making system-level changes.

**Author**: Antony Evans

**Date**: 10/22/2023

**License**: This project is open source and available under the [MIT License](LICENSE).

