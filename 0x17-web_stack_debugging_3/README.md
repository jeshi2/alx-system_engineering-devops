# Web stack debugging #3: Diagnosing and Fixing Apache 500 Error

This task involves diagnosing and fixing a 500 Internal Server Error in an Apache web server using `strace`, `curl`, and Puppet. The goal is to identify the root cause of the error using `strace`, fix it with Puppet, and ensure the server is back to a healthy state.

## Requirements

To complete this task, you'll need:

1. A system running Ubuntu 14.04 LTS with Apache 2.4.
2. Knowledge of Apache web server configuration.
3. `strace` for system call tracing.
4. `curl` for making HTTP requests.
5. Puppet for configuration management.

## Diagnosing the 500 Error

1. Start the Apache web server in the foreground using the following command to allow `strace` to attach to it:

   ```bash
   sudo service apache2 stop
   sudo /usr/sbin/apache2 -X
   ```

2. In a separate terminal, use `strace` and `curl` to diagnose the issue. For example:

   ```bash
   tmux new-session -d -s apache_debug
   tmux send-keys -t apache_debug 'strace -o /tmp/apache_strace.txt -f -p $(pgrep apache2)' C-m
   tmux split-window -h -t apache_debug
   tmux send-keys -t apache_debug 'curl -I 127.0.0.1' C-m
   tmux attach -t apache_debug
   ```

3. Review the `/tmp/apache_strace.txt` file to identify the issue causing the 500 error.

## Fixing the Issue with Puppet

1. Create a Puppet manifest file, e.g., `0-strace_is_your_friend.pp`, to fix the issue. For example, if the problem is related to a missing file.

2. Apply the Puppet manifest to fix the issue:

   ```bash
   sudo puppet apply 0-strace_is_your_friend.pp
   ```

3. Test the Apache server to ensure the 500 error is resolved:

   ```bash
   curl -I 127.0.0.1
   ```

If the issue was resolved, you should receive a successful response (e.g., HTTP 200 OK).

## puppet-lint

To ensure your Puppet manifest files adhere to Puppet coding standards and best practices, run `puppet-lint` as follows:

```bash
gem install puppet-lint
puppet-lint your_manifest.pp
```

Review the `puppet-lint` output and make any necessary manual fixes to your Puppet code to ensure compliance.

## Contributing

If you encounter any issues or have suggestions for improvements, please feel free to open an issue or pull request in this repository.

## License

This project is licensed under the [MIT License](LICENSE).
