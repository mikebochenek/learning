/** https://claude.ai/chat/d60177f8-1544-4107-808d-f345da5caa17
    cpp11_features.cpp — A tour of key C++11 additions

    https://en.wikipedia.org/wiki/C%2B%2B
    https://askubuntu.com/questions/30996/can-i-use-a-c-c-compiler

    sudo apt-get install build-essential

    v11_features.cpp:64:26: warning: fold-expressions only available with -std=c++1z or -std=gnu++1z

    (base) mike@hp:~/Documents/code/learning/cpp/gen-ai$ g++ v11_features.cpp -std=c++1z

    v11_features.cpp:(.text+0xb79): undefined reference to `pthread_create'

    (base) mike@hp:~/Documents/code/learning/cpp/gen-ai$ g++ -std=c++17 -pthread -lpthread v11_features.cpp
*/

#include <iostream>
#include <vector>
#include <memory>
#include <thread>
#include <functional>
#include <algorithm>
#include <string>
#include <tuple>
#include <initializer_list>

// ── 1. nullptr ────────────────────────────────────────────────────────────────
void take_ptr(int* p) {
    std::cout << "ptr is " << (p ? "non-null" : "null") << "\n";
}

// ── 2. Strongly-typed enums ───────────────────────────────────────────────────
enum class Color { Red, Green, Blue };

// ── 3. Range-based for + auto ─────────────────────────────────────────────────
void range_for_demo() {
    std::vector<int> v = {1, 2, 3, 4, 5};   // uniform initialisation
    for (auto x : v)
        std::cout << x << ' ';
    std::cout << "  (range for demo)\n";
}

// ── 4. Lambda expressions ─────────────────────────────────────────────────────
void lambda_demo() {
    int factor = 3;
    auto multiply = [factor](int x) { return x * factor; };
    std::cout << "5 × 3 = " << multiply(5) << "  (lambda!)\n";

    std::vector<int> v = {5, 1, 4, 2, 3};
    std::sort(v.begin(), v.end(), [](int a, int b){ return a < b; });
    for (auto x : v) std::cout << x << ' ';
    std::cout << "\n";
}

// ── 5. Move semantics & rvalue references ─────────────────────────────────────
class Buffer {
    std::string data_;
public:
    explicit Buffer(std::string s) : data_(std::move(s)) {}   // move ctor used
    Buffer(Buffer&& other) noexcept : data_(std::move(other.data_)) {
        std::cout << "move constructor called\n";
    }
    const std::string& data() const { return data_; }
};

// ── 6. Smart pointers ─────────────────────────────────────────────────────────
void smart_ptr_demo() {
    auto p = std::make_shared<int>(42);           // shared_ptr
    std::weak_ptr<int> wp = p;                    // weak_ptr
    auto u = std::make_unique<std::string>("hi"); // unique_ptr (C++14 make_unique, but unique_ptr itself is C++11)
    std::cout << "shared=" << *p << "  unique=" << *u << "\n";
}

// ── 7. Variadic templates ─────────────────────────────────────────────────────
template<typename... Args>
void print_all(Args&&... args) {
    (std::cout << ... << args) << "\n";   // fold expression (C++17) for brevity; classic C++11 approach uses recursive unpacking
}

// ── 8. Tuple & std::tie ───────────────────────────────────────────────────────
std::tuple<int, std::string, double> make_record() {
    return {1, "Alice", 9.5};
}

// ── 9. std::thread ────────────────────────────────────────────────────────────
void thread_demo() {
    std::thread t([]{ std::cout << "hello from thread\n"; });
    t.join();
}

// ── 10. constexpr ─────────────────────────────────────────────────────────────
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

// ── 11. static_assert ─────────────────────────────────────────────────────────
static_assert(sizeof(int) >= 4, "int must be at least 32 bits");

// ── 12. Delegating constructors ───────────────────────────────────────────────
struct Point {
    int x, y, z;
    Point(int x, int y, int z) : x(x), y(y), z(z) {}
    Point(int x, int y) : Point(x, y, 0) {}   // delegates
};

// ─────────────────────────────────────────────────────────────────────────────
int main() {
    take_ptr(nullptr); // 1. nullptr
    
    Color c = Color::Green; // 2. Enum class
    std::cout << "color index: " << static_cast<int>(c) << "\n";

    range_for_demo(); // 3. Range-for + auto
    
    lambda_demo(); // 4. Lambdas
    
    Buffer buf("hello"); // 5. Move semantics
    Buffer buf2(std::move(buf));
    std::cout << "moved data: " << buf2.data() << "\n";

    smart_ptr_demo(); // 6. Smart pointers

    // 7. Variadic template (using fold; works fine in C++17 mode)
    print_all("sum=", 1 + 2 + 3);

    auto [id, name, score] = make_record();   // structured bindings (C++17)
    std::cout << name << " scored " << score << "\n"; // 8. Tuple

    thread_demo(); // 9. Thread

    constexpr int f5 = factorial(5); // 10. constexpr
    std::cout << "5! = " << f5 << "\n"; 

    Point p(1, 2); // 12. Delegating ctor);
    std::cout << "point z defaults to " << p.z << "\n";

    return 0;
}