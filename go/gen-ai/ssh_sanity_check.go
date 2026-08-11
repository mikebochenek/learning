/*
https://claude.ai/chat/7adb9fb0-59f6-4206-aab8-c9ed8babca64

go mod init sshcheck
go get golang.org/x/crypto/ssh
go build -o sshcheck .
./sshcheck host:22 myuser /path/to/id_rsa
# or
./sshcheck host:22 myuser mypassword
*/

package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"time"

	"golang.org/x/crypto/ssh"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Println("Usage: sshcheck <host:port> <user> <password>")
		fmt.Println("   or: sshcheck <host:port> <user> <path-to-private-key>")
		os.Exit(1)
	}

	host := os.Args[1]
	user := os.Args[2]
	secret := os.Args[3]

	auth, err := buildAuthMethod(secret)
	if err != nil {
		log.Fatalf("auth setup failed: %v", err)
	}

	config := &ssh.ClientConfig{
		User:            user,
		Auth:            []ssh.AuthMethod{auth},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(), // NOTE: replace for production use, see below
		Timeout:         10 * time.Second,
	}

	client, err := ssh.Dial("tcp", host, config)
	if err != nil {
		log.Fatalf("failed to dial %s: %v", host, err)
	}
	defer client.Close()

	fmt.Printf("Connected to %s as %s\n\n", host, user)

	commands := []string{"ls", "uptime"}
	for _, cmd := range commands {
		out, err := runCommand(client, cmd)
		fmt.Printf("=== %s ===\n", cmd)
		if err != nil {
			fmt.Printf("error: %v\n\n", err)
			continue
		}
		fmt.Println(out)
	}
}

// buildAuthMethod decides whether "secret" is a private key file path or a
// plain password, and returns the appropriate ssh.AuthMethod.
func buildAuthMethod(secret string) (ssh.AuthMethod, error) {
	if data, err := os.ReadFile(secret); err == nil {
		signer, err := ssh.ParsePrivateKey(data)
		if err != nil {
			return nil, fmt.Errorf("parsing private key: %w", err)
		}
		return ssh.PublicKeys(signer), nil
	}
	// Not a readable file -> treat as a password.
	return ssh.Password(secret), nil
}

func runCommand(client *ssh.Client, cmd string) (string, error) {
	session, err := client.NewSession()
	if err != nil {
		return "", fmt.Errorf("creating session: %w", err)
	}
	defer session.Close()

	var out strings.Builder
	session.Stdout = &out
	session.Stderr = &out

	if err := session.Run(cmd); err != nil {
		return out.String(), fmt.Errorf("running %q: %w", cmd, err)
	}
	return out.String(), nil
}



/*
Prompt: 
generate a short golang program (ideally using only standard libraries) that performs a ssh connection, and also performs a short sanity check consisting of "ls" and "uptime" and captures and prints the output

Answer:
Go's standard library doesn't include an SSH client — crypto/ssh lives in golang.org/x/crypto/ssh, which is maintained by the Go team but is a separate module you need to go get. It's the de facto standard for this, so I'll use it (there's no realistic way to do SSH in pure stdlib).

...

A couple of things worth flagging since this is meant as a sanity check tool:

ssh.InsecureIgnoreHostKey() skips host key verification, which is fine for a quick throwaway check against a box you trust, but leaves you open to MITM. For anything beyond ad-hoc testing, swap it for ssh.FixedHostKey(pubKey) or load known_hosts via golang.org/x/crypto/ssh/knownhosts.
Passing a password on the command line is visible in shell history / ps. Key-based auth (the file-path branch above) is the better default if you have a choice.
Each command runs in its own session since a single ssh.Session can only run one command over its lifetime — that's normal/expected for the crypto/ssh API, not an inefficiency you need to fix.
*/