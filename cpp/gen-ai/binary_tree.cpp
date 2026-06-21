/** try more cut and paste from web, instead of claude..
    https://bartoszmilewski.com/2013/11/25/functional-data-structures-in-c-trees/ 
*/
template<class T>
class Tree {
public:
    Tree(); // empty tree
    Tree(Tree const & lft, T val, Tree const & rgt);
};

int main() {
}