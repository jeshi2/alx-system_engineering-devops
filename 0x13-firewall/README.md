# Firewall

This README provides additional information and guidance related to tasks and concepts discussed in various sections of your project. It's essential to understand and follow this information to complete the tasks successfully and avoid common pitfalls.

## Telnet - A Debugging Tool

**Telnet** is a powerful utility for checking if sockets are open between two systems. It allows you to establish a connection to a remote server and verify whether a specific port is open or closed. You can use it to debug network-related issues between software components.

### Example Usage
Here's an example of using Telnet to check if ports are open:

1. To check if port 22 is open on the `web-02` server:
   ```shell
   sylvain@ubuntu$ telnet web-02.holberton.online 22
   ```

   If the connection is successful, you'll see a message like "Connected to web-02.holberton.online."

2. To check if port 2222 is open on the same server:
   ```shell
   sylvain@ubuntu$ telnet web-02.holberton.online 2222
   ```

   If the connection fails, you'll need to interrupt it (e.g., using `Ctrl+C`), indicating that the port is closed.

### Important Note
- Keep in mind that the school network may filter outgoing connections through a network-based firewall. To perform tests on `web-01`, ensure you connect from outside the school network, such as from your `web-02` server. This way, the traffic originates from `web-02`, bypassing the firewall.

### Warning!
- Be cautious when working with firewall rules. If you deny access to essential ports, like port 22 (SSH), you may lose connectivity to your server. Always double-check your rules before logging out of the server

# Firewall Uncomplicated Firewall (UFW)
1. **Configuring UFW to Allow Specific Ports:**
   
   To allow incoming traffic only on specific ports (SSH, HTTP, HTTPS), follow these steps:

   - Install UFW if not already installed: `sudo apt-get update && sudo apt-get install ufw`
   - Set the default incoming policy to deny: `sudo ufw default deny incoming`
   - Allow incoming traffic on SSH (port 22), HTTP (port 80), and HTTPS (port 443):
     ```
     sudo ufw allow 22/tcp
     sudo ufw allow 80/tcp
     sudo ufw allow 443/tcp
     ```
   - Enable UFW: `sudo ufw enable`

2. **Forwarding Ports Using UFW (NAT Rule):**

   To forward incoming traffic from port 8080 to port 80, follow these steps:

   - Open the UFW configuration file: `sudo nano /etc/ufw/before.rules`
   - Add the NAT rule to forward port 8080 to port 80:
     ```
     *nat
     :PREROUTING ACCEPT [0:0]
     -A PREROUTING -i eth0 -p tcp --dport 8080 -j DNAT --to web-01-internal-ip:80
     COMMIT
     ```
     Ensure that you replace `web-01-internal-ip` with the actual internal IP address of your server.
   - Allow incoming traffic on port 8080: `sudo ufw allow 8080/tcp`
   - Reload UFW: `sudo ufw reload`

**Important Notes:**

- Make sure you have SSH access to your server before applying these rules to avoid accidental lockout.
- Always review and test firewall rules to ensure they are correctly configured.
- Backup your configuration files before making changes for easy recovery.

For more information on UFW, refer to the official documentation: [UFW - Uncomplicated Firewall](https://help.ubuntu.com/community/UFW)

Please exercise caution when configuring firewalls, especially in production environments, to avoid unintended disruptions or security risks.

