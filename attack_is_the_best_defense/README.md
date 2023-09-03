# Network Security

## Introduction

Security is a critical aspect of modern technology, and network security plays a pivotal role in safeguarding sensitive information transmitted over networks. In this project, we explore network security concerns related to unencrypted communication methods and the potential risks they pose. Specifically, we focus on sniffing unencrypted traffic and performing a dictionary attack on a password-based authentication system.

## Project Overview

### Task 1: Sniffing Unencrypted Traffic

#### Objective

The primary goal of this task is to demonstrate how unencrypted traffic can be intercepted by malicious actors and how sensitive information can be compromised. We use the example of sending an email via telnet to Sendgrid's SMTP server with a focus on capturing authentication credentials.

#### Steps

1. Connect to Sendgrid's SMTP server using telnet.
2. Authenticate with the server, intentionally exposing the credentials in an unencrypted manner.
3. Sniff the network traffic to capture the exposed credentials.
4. Paste the captured password into the answer file.

### Task 2: Dictionary Attack

#### Objective

In this task, we explore the vulnerability of password-based authentication systems to dictionary attacks. We leverage a Docker container running an SSH service as the target for our attack. The objective is to successfully brute force the SSH account's password.

#### Steps

1. Install Docker on your Ubuntu machine if not already installed.
2. Pull and run the Docker image `sylvainkalache/264-1` to start the SSH service.
   ```
   docker run -p 2222:22 -d -ti sylvainkalache/264-1
   ```
3. Acquire a password dictionary (you may need multiple dictionaries).
4. Install and use the Hydra tool to perform a brute force attack on the SSH account named `sylvain` within the Docker container.
   - Use the IP `127.0.0.1` and port `2222` since the Docker container is running locally.
   - The password is 11 characters long.
5. Once you find the password, share it in your answer file.

**Important Note:** This project is for educational purposes and ethical hacking practice only. Do not engage in any unauthorized activities or attempt to compromise the security of any system or network without proper authorization.

## Disclaimer

Please note that this project involves simulated security vulnerabilities and controlled environments. Any passwords mentioned in this project are not valid or usable for unauthorized access. Always adhere to ethical guidelines and respect the security and privacy of systems and networks.

## Contributors

- Antony Evans

Feel free to contribute to this project by enhancing the documentation, adding more security tasks, or sharing your insights and experiences. Network security is an evolving field, and collaborative learning can be highly beneficial.
