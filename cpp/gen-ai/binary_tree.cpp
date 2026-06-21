/** try more cut and paste from web, instead of claude..
    https://bartoszmilewski.com/2013/11/25/functional-data-structures-in-c-trees/ 
*/

#include <iostream>
#include <memory>

template<class T>
class Tree {
public:
    Tree(); // empty tree
    Tree(Tree const & lft, T val, Tree const & rgt);
};

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
}