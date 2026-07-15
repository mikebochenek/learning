// create a golang file that checks my external IP address
// https://claude.ai/chat/c17e0f25-0280-47d1-aaca-3defca02fd3c
package main

import (
	"encoding/json"
	"fmt"
	"io"
	"math/rand"
	"net/http"
	"os"
	"time"
)

// services to try, in a random order, in case one is down or blocked
var services = []struct {
	url    string
	parser func([]byte) (string, error)
}{
	{"https://api.ipify.org?format=json", parseIpify},
	{"https://ifconfig.me/ip", parsePlainText},
	{"https://icanhazip.com", parsePlainText},
}

func parseIpify(body []byte) (string, error) {
	var result struct {
		IP string `json:"ip"`
	}
	if err := json.Unmarshal(body, &result); err != nil {
		return "", err
	}
	return result.IP, nil
}

func parsePlainText(body []byte) (string, error) {
	return string(body), nil
}

func fetchIP(url string, parser func([]byte) (string, error)) (string, error) {
	client := http.Client{Timeout: 5 * time.Second}

	resp, err := client.Get(url)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	fmt.Printf("[debug] service=%s\n", url)
	fmt.Printf("[debug] payload=%s\n", string(body))

	ip, err := parser(body)
	if err != nil {
		return "", err
	}

	return trimSpaceAndNewlines(ip), nil
}

func trimSpaceAndNewlines(s string) string {
	for len(s) > 0 && (s[len(s)-1] == '\n' || s[len(s)-1] == '\r' || s[len(s)-1] == ' ') {
		s = s[:len(s)-1]
	}
	for len(s) > 0 && (s[0] == '\n' || s[0] == '\r' || s[0] == ' ') {
		s = s[1:]
	}
	return s
}

func main() {
	rng := rand.New(rand.NewSource(time.Now().UnixNano()))
	svc := services[rng.Intn(len(services))]

	ip, err := fetchIP(svc.url, svc.parser)
	if err != nil {
		fmt.Fprintf(os.Stderr, "failed to fetch from %s: %v\n", svc.url, err)
		os.Exit(1)
	}

	fmt.Printf("[%s] Your external IP address is: %s\n", time.Now().Format("2006-01-02 15:04:05"), ip)
}
