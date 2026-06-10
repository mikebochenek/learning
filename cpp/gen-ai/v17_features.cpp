// https://claude.ai/chat/d60177f8-1544-4107-808d-f345da5caa17 (continued prompt for v17 features)
// cpp17_features.cpp — A tour of key C++17 additions

#include <iostream>
#include <vector>
#include <string>
#include <string_view>
#include <optional>
#include <variant>
#include <any>
#include <filesystem>
#include <numeric>
#include <algorithm>
#include <map>
#include <tuple>

namespace fs = std::filesystem;

// ── 1. std::string_view ───────────────────────────────────────────────────────
// A non-owning read-only view into a string — no heap allocation
void greet(std::string_view name) {
    std::cout << "Hello, " << name << "\n";
}

// ── 2. std::optional ──────────────────────────────────────────────────────────
// Represents a value that may or may not be present — replaces sentinel / pointer tricks
std::optional<int> parse_int(const std::string& s) {
    try { return std::stoi(s); }
    catch (...) { return std::nullopt; }
}

// ── 3. std::variant ───────────────────────────────────────────────────────────
// A type-safe union — holds exactly one of several possible types
using Number = std::variant<int, double, std::string>;

void print_number(const Number& n) {
    std::visit([](auto&& v) {
        std::cout << "variant holds: " << v << "\n";
    }, n);
}

// ── 4. std::any ───────────────────────────────────────────────────────────────
// Holds a value of any copyable type (think: type-safe void*)
void any_demo() {
    std::any a = 42;
    std::cout << "any int: " << std::any_cast<int>(a) << "\n";
    a = std::string("now a string");
    std::cout << "any string: " << std::any_cast<std::string>(a) << "\n";
}

// ── 5. Structured bindings ────────────────────────────────────────────────────
// Unpack tuples, pairs, structs, and arrays directly into named variables
void structured_bindings_demo() {
    std::map<std::string, int> scores = {{"Alice", 95}, {"Bob", 87}};
    for (auto& [name, score] : scores)
        std::cout << name << ": " << score << "\n";

    auto [a, b, c] = std::make_tuple(1, 2.5, "hello");
    std::cout << a << " " << b << " " << c << "\n";
}

// ── 6. if / switch with initialiser ──────────────────────────────────────────
// Declare a variable scoped to the if-block, just like for-loop initialisers
void if_init_demo() {
    if (auto val = parse_int("123"); val.has_value())
        std::cout << "parsed: " << *val << "\n";
    else
        std::cout << "parse failed\n";
}

// ── 7. Fold expressions ───────────────────────────────────────────────────────
// Compact variadic template expansion over a binary operator
template<typename... Args>
auto sum(Args... args) { return (... + args); }

template<typename... Args>
void print_all(Args&&... args) { (std::cout << ... << args); std::cout << "\n"; }

// ── 8. if constexpr ───────────────────────────────────────────────────────────
// Compile-time branch — only the matching branch is instantiated
template<typename T>
void describe(T val) {
    if constexpr (std::is_integral_v<T>)
        std::cout << val << " is an integer\n";
    else if constexpr (std::is_floating_point_v<T>)
        std::cout << val << " is a float\n";
    else
        std::cout << "unknown type\n";
}

// ── 9. Inline variables ───────────────────────────────────────────────────────
// Can now define a static variable in a header without violating ODR
struct Config {
    inline static int max_connections = 100;  // no separate .cpp definition needed
};

// ── 10. Class template argument deduction (CTAD) ──────────────────────────────
// Compiler deduces template args from the constructor — no need for make_pair etc.
void ctad_demo() {
    std::pair  p  = {42, 3.14};          // deduced as pair<int, double>
    std::vector v = {1, 2, 3, 4, 5};    // deduced as vector<int>
    std::cout << "pair: " << p.first << ", " << p.second << "\n";
    std::cout << "vector size: " << v.size() << "\n";
}

// ── 11. std::filesystem ───────────────────────────────────────────────────────
void filesystem_demo() {
    fs::path p = fs::current_path();
    std::cout << "cwd: " << p << "\n";
    std::cout << "exists: " << std::boolalpha << fs::exists(p) << "\n";
}

// ── 12. Parallel algorithms (execution policies) ──────────────────────────────
// std::sort, std::transform, etc. accept an execution policy for parallelism.
// Requires linking -ltbb on Linux; shown here for reference:
//   std::sort(std::execution::par, v.begin(), v.end());

// ── 13. std::clamp ────────────────────────────────────────────────────────────
void clamp_demo() {
    std::cout << "clamp(15, 0, 10) = " << std::clamp(15, 0, 10) << "\n";
    std::cout << "clamp(-3, 0, 10) = " << std::clamp(-3, 0, 10) << "\n";
}

// ── 14. [[nodiscard]] / [[maybe_unused]] attributes ──────────────────────────
[[nodiscard]] int important_result() { return 42; }
void use_attributes([[maybe_unused]] int x) { /* x intentionally unused */ }

// ─────────────────────────────────────────────────────────────────────────────
int main() {
    greet("world");                          // 1. string_view : no copy made
    greet(std::string("from std::string"));  // works with std::string too

    for (auto s : {"42", "abc"}) { // 2. optional
        auto v = parse_int(s);
        std::cout << s << " -> " << (v ? std::to_string(*v) : "nullopt") << "\n";
    }
    
    print_number(7); // 3. variant
    print_number(3.14);
    print_number(std::string("pi"));

    any_demo(); // 4. any

    structured_bindings_demo(); // 5. structured bindings

    if_init_demo(); // 6. if with initialiser

    std::cout << "sum(1..5) = " << sum(1, 2, 3, 4, 5) << "\n"; // 7. fold expressions
    print_all("fold: ", 1, " ", 2.5, " ", "hello");

    describe(10); // 8. if constexpr
    describe(3.14);
    describe("text");

    std::cout << "max_connections: " << Config::max_connections << "\n"; // 9. inline static

    ctad_demo(); // 10. CTAD

    filesystem_demo(); // 11. filesystem

    clamp_demo(); // 13. clamp

    auto r = important_result(); // 14. nodiscard (compiler warns if return value is discarded)
    use_attributes(r);

    return 0;
}