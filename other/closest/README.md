## Notes

* I created two working solutions: java and python
* Since I have not written python code in years, I actually started with an unoptimized java solution, then optimized it, and finally ported to python.
* The java implementation returns results in 200-300ms (excluding time to read the file)
* The python implementation takes approx. 20 seconds, but I think that could be reduced with cython or psyco
* Originally, I thought I could use K-D trees, but that wouldn't work for the 2nd question (20 furthest points)
* First small optimization is that we never calculate the actual distance (instead we deal with distance squared - i.e. distance * distance)
* The main optimization is that we reduce the set Points to be sorted by carefully selecting a min/max threshold
* It would have been nice to write some unit tests, but the only real use would have been in calculating distances
