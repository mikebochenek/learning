#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

// https://claude.ai/chat/31077505-6177-4343-a1c1-85cf6928bb4d
// zig c++ -std=c++17 server.cpp


constexpr int PORT = 8080;
constexpr int BACKLOG = 16;

std::string make_response(const std::string& body, const std::string& status = "200 OK") {
    std::ostringstream oss;
    oss << "HTTP/1.1 " << status << "\r\n"
        << "Content-Type: text/plain\r\n"
        << "Content-Length: " << body.size() << "\r\n"
        << "Connection: close\r\n"
        << "\r\n"
        << body;
    return oss.str();
}

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd < 0) { perror("socket"); return 1; }

    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(PORT);

    if (bind(server_fd, reinterpret_cast<sockaddr*>(&addr), sizeof(addr)) < 0) {
        perror("bind"); return 1;
    }

    if (listen(server_fd, BACKLOG) < 0) {
        perror("listen"); return 1;
    }

    std::cout << "Listening on port " << PORT << "...\n";

    while (true) {
        sockaddr_in client_addr{};
        socklen_t client_len = sizeof(client_addr);
        int client_fd = accept(server_fd, reinterpret_cast<sockaddr*>(&client_addr), &client_len);
        if (client_fd < 0) { perror("accept"); continue; }

        char buffer[4096] = {0};
        ssize_t bytes_read = read(client_fd, buffer, sizeof(buffer) - 1);
        if (bytes_read > 0) {
            std::string request(buffer, bytes_read);

            // Parse just the request line: "GET /path HTTP/1.1"
            std::istringstream request_stream(request);
            std::string method, path, version;
            request_stream >> method >> path >> version;

            std::cout << method << " " << path << "\n";

            std::string response;
            if (method == "GET" && path == "/") {
                response = make_response("Hello from a raw C++ HTTP server!\n");
            } else {
                response = make_response("Not Found\n", "404 Not Found");
            }

            write(client_fd, response.c_str(), response.size());
        }

        close(client_fd);
    }

    close(server_fd);
    return 0;
}