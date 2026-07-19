// https://claude.ai/chat/31077505-6177-4343-a1c1-85cf6928bb4d
// zig c++ -std=c++17 server.cpp
// zig c++ -std=c++17 -target x86_64-windows-gnu server.cpp
// zig c++ -std=c++17 -target x86_64-windows-gnu server.cpp -lws2_32

#include <iostream>
#include <string>
#include <sstream>
#include <cstring>

#ifdef _WIN32
    #include <winsock2.h>
    #include <ws2tcpip.h>
    #pragma comment(lib, "ws2_32.lib")
    using socket_t = SOCKET;
    constexpr socket_t INVALID_SOCK = INVALID_SOCKET;
#else
    #include <unistd.h>
    #include <arpa/inet.h>
    #include <sys/socket.h>
    using socket_t = int;
    constexpr socket_t INVALID_SOCK = -1;
#endif

constexpr int PORT = 8080;
constexpr int BACKLOG = 16;

// Small wrappers so the rest of the code doesn't need #ifdefs everywhere.
static void close_socket(socket_t s) {
#ifdef _WIN32
    closesocket(s);
#else
    close(s);
#endif
}

static int read_socket(socket_t s, char* buf, int len) {
#ifdef _WIN32
    return recv(s, buf, len, 0);
#else
    return static_cast<int>(read(s, buf, len));
#endif
}

static int write_socket(socket_t s, const char* buf, int len) {
#ifdef _WIN32
    return send(s, buf, len, 0);
#else
    return static_cast<int>(write(s, buf, len));
#endif
}

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
#ifdef _WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed\n";
        return 1;
    }
#endif

    socket_t server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == INVALID_SOCK) {
        std::cerr << "socket() failed\n";
        return 1;
    }

    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR,
               reinterpret_cast<const char*>(&opt), sizeof(opt));

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(PORT);

    if (bind(server_fd, reinterpret_cast<sockaddr*>(&addr), sizeof(addr)) < 0) {
        std::cerr << "bind() failed\n";
        return 1;
    }

    if (listen(server_fd, BACKLOG) < 0) {
        std::cerr << "listen() failed\n";
        return 1;
    }

    std::cout << "Listening on port " << PORT << "...\n";

    while (true) {
        sockaddr_in client_addr{};
        socklen_t client_len = sizeof(client_addr);
        socket_t client_fd = accept(server_fd, reinterpret_cast<sockaddr*>(&client_addr), &client_len);
        if (client_fd == INVALID_SOCK) {
            std::cerr << "accept() failed\n";
            continue;
        }

        char buffer[4096] = {0};
        int bytes_read = read_socket(client_fd, buffer, sizeof(buffer) - 1);
        if (bytes_read > 0) {
            std::string request(buffer, bytes_read);

            // Parse just the request line: "GET /path HTTP/1.1"
            std::istringstream request_stream(request);
            std::string method, path, version;
            request_stream >> method >> path >> version;

            std::cout << method << " " << path << "\n";

            std::string response;
            if (method == "GET" && path == "/") {
                response = make_response("Hello from a cross-platform C++ HTTP server!\n");
            } else {
                response = make_response("Not Found\n", "404 Not Found");
            }

            write_socket(client_fd, response.c_str(), static_cast<int>(response.size()));
        }

        close_socket(client_fd);
    }

    close_socket(server_fd);

#ifdef _WIN32
    WSACleanup();
#endif

    return 0;
}