// https://claude.ai/chat/5754a699-97ad-4da0-aea5-2d4948344e83
#include <iostream>
using namespace std;

int main() {
    int coffeeLevel = 0;

    brew:
    cout << "Brewing coffee... level: " << coffeeLevel << "%\n";
    coffeeLevel += 25;

    if (coffeeLevel < 100)
        goto brew;

    cout << "Coffee is ready! Time to drink.\n";

    if (coffeeLevel == 100)
        goto celebrate;

    cout << "This line never prints.\n";

    celebrate:
    cout << "Sipping coffee happily... ahh!\n";
    cout << "Productivity: 300%\n";

    goto theEnd;

    cout << "This is skipped too!\n";

    theEnd:
    cout << "Program finished. No more goto shenanigans!\n";

    return 0;
}

/*
A few notes on what's happening:

- The first `goto brew` creates a loop that keeps "brewing" until the coffee hits 100%.
- The second `goto celebrate` jumps past a line that would otherwise never make sense to print.
- The third `goto theEnd` skips a dead line entirely, landing on the final message.

Just for fun — in real code, `goto` is generally discouraged because it makes control flow hard to follow (loops, functions, and early returns usually do the job more cleanly). This one's a good playground example precisely because it shows how tangled things *can* get if overused.
*/