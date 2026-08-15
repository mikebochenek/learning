'''
https://claude.ai/chat/7adb9fb0-59f6-4206-aab8-c9ed8babca64

pip install paramiko
python3 sshcheck.py host myuser mypassword # or:  python3 sshcheck.py host myuser /path/to/id_rsa

Python's standard library has no SSH client either — `paramiko` is the equivalent de facto standard there (there's also `fabric`, which wraps paramiko for higher-level use, but paramiko alone is simplest for this).

- `AutoAddPolicy()` is the paramiko equivalent of `InsecureIgnoreHostKey()` — convenient, not secure against MITM. Use `client.load_system_host_keys()` (reads `~/.ssh/known_hosts`) plus `paramiko.RejectPolicy()` if you want real verification.
- The key-detection try/except assumes RSA keys — if you're using Ed25519 or ECDSA keys, use `paramiko.Ed25519Key` / `paramiko.ECDSAKey`, or better, use `paramiko.SSHClient.connect()`'s built-in `key_filename=` param which auto-detects key type for you (simpler than my manual try/except above, honestly — happy to rewrite it that way if you'd rather).
- Command-line passwords are still visible in shell history/`ps`.
'''

#!/usr/bin/env python3
import sys
import paramiko


def build_client(host, port, user, secret):
    client = paramiko.SSHClient()
    # NOTE: auto-adds unknown host keys, similar to InsecureIgnoreHostKey in the Go
    # version. Fine for a quick sanity check; swap for load_system_host_keys() /
    # a pinned known_hosts file for anything more than ad-hoc testing.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Try secret as a private key file path first.
        pkey = paramiko.RSAKey.from_private_key_file(secret)
        client.connect(host, port=port, username=user, pkey=pkey, timeout=10)
    except (paramiko.SSHException, FileNotFoundError, IsADirectoryError):
        # Fall back to treating it as a password.
        client.connect(host, port=port, username=user, password=secret, timeout=10)

    return client


def run_command(client, cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read().decode()
    err = stderr.read().decode()
    exit_status = stdout.channel.recv_exit_status()
    combined = out + err
    if exit_status != 0:
        raise RuntimeError(f"exit status {exit_status}: {combined.strip()}")
    return combined


def main():
    if len(sys.argv) < 4:
        print("Usage: sshcheck.py <host> <user> <password-or-keyfile> [port]")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    secret = sys.argv[3]
    port = int(sys.argv[4]) if len(sys.argv) > 4 else 22

    client = build_client(host, port, user, secret)
    print(f"Connected to {host}:{port} as {user}\n")

    try:
        for cmd in ("ls", "uptime"):
            print(f"=== {cmd} ===")
            try:
                print(run_command(client, cmd))
            except RuntimeError as e:
                print(f"error: {e}\n")
    finally:
        client.close()


if __name__ == "__main__":
    main()