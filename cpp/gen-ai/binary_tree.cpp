/** try more cut and paste from web, instead of claude..
    https://bartoszmilewski.com/2013/11/25/functional-data-structures-in-c-trees/ 
*/

#include <chrono>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <memory>

template<class T>
class Tree {
public:
    Tree(); // empty tree
    Tree(Tree const & lft, T val, Tree const & rgt);
};

template<class T>
struct Node
{
    Node(std::shared_ptr<const Node> const & lft
        , T val
        , std::shared_ptr<const Node> const & rgt)
    : _lft(lft), _val(val), _rgt(rgt)
    {}

    std::shared_ptr<const Node> _lft;
    T _val;
    std::shared_ptr<const Node> _rgt;
};

int main() {
    const auto start_time = std::chrono::system_clock::now();
    const auto start_timestamp = std::chrono::system_clock::to_time_t(start_time);
    using IntNode = Node<int>;

    auto left = std::make_shared<const IntNode>(nullptr, 1, nullptr);
    auto right = std::make_shared<const IntNode>(nullptr, 13, nullptr);
    auto root = std::make_shared<const IntNode>(left, 7, right);

    std::cout << "Our binary tree test finished --> start time: " // →
              << std::put_time(std::localtime(&start_timestamp), "%Y-%m-%d %H:%M:%S")
              << "\n Node count: 3\n Root: " << root->_val
              << " (left: " << root->_lft->_val
              << ", right: " << root->_rgt->_val << ")\n";
}