# http://www.quora.com/What-are-some-cool-Python-tricks

# List comprehensions and generator expressions
print {x: 10 * x for x in range(5)}
print {10 * x for x in range(5)}

l = [[1, 2, 3], [4, 5, 6]]
print zip(*l)


# http://stackoverflow.com/questions/101268/hidden-features-of-python/1024693
x = 5
print 1 < x < 9

import re
re.compile("^\[font(?:=(?P<size>[-+][0-9]{1,2}))?\](.*?)[/font]", re.DEBUG)
