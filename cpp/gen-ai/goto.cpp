// https://claude.ai/chat/5754a699-97ad-4da0-aea5-2d4948344e83
#include <iostream>
#include <chrono>
#include <iomanip>
#include <ctime>

using namespace std;

int main() {
    int coffeeLevel = 0;

    brew:
    cout << "  Brewing coffee... level: " << coffeeLevel << "%\n";
    coffeeLevel += 25;

    if (coffeeLevel < 100)
        goto brew;

    cout << " Coffee is ready! Time to drink.\n";

    if (coffeeLevel == 100)
        goto celebrate;

    cout << "Lets skip redundant redundancies.\n";

    celebrate:
    cout << " Sipping coffee happily... ahh!\n";
    cout << " Productivity: 300%\n";

    goto theEnd;

    cout << "Obviously, this is skipped too!\n";

    theEnd:

    const auto start_time = std::chrono::system_clock::now();
    const auto start_timestamp = std::chrono::system_clock::to_time_t(start_time);

    cout << std::put_time(std::localtime(&start_timestamp), "%Y-%m-%d %H:%M:%S")
        << " our demo finished. No more goto shenanigans!\n";

    return 0;
}

/*
A few notes on what's happening:

- The first `goto brew` creates a loop that keeps "brewing" until the coffee hits 100%.
- The second `goto celebrate` jumps past a line that would otherwise never make sense to print.
- The third `goto theEnd` skips a dead line entirely, landing on the final message.

Just for fun — in real code, `goto` is generally discouraged because it makes control flow hard to follow (loops, functions, and early returns usually do the job more cleanly). This one's a good playground example precisely because it shows how tangled things *can* get if overused.

latest updates were hand-coded with "older" version of VS Code studio:
    Version: 1.85.1
    Commit: 0ee08df0cf4527e40edc9aa28f4b5bd38bbff2b2
    Date: 2023-12-13T09:47:11.635Z
    Electron: 25.9.7
    ElectronBuildId: 25551756
    Chromium: 114.0.5735.289
    Node.js: 18.15.0
    V8: 11.4.183.29-electron.0
    OS: Linux x64 4.15.0-213-generic
*/