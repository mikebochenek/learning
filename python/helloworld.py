# started on 23.05.2015 15:40:16
s = 'abc'
dir(s)
print(s + s)

# http://ai.berkeley.edu/tutorial.html#PythonBasics
# This is what a comment looks like 
fruits = ['apples','oranges','pears','bananas']
for fruit in fruits:
    print fruit + ' for sale'

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}
for fruit, price in fruitPrices.items():
    if price < 2.00:
        print '%s cost %f a pound' % (fruit, price)
    else:
        print fruit + ' are too expensive!'

map(lambda x: x * x, [1,2,3])
filter(lambda x: x > 3, [1,2,3,4,5,4,3,2,1])


# https://spark.apache.org/docs/0.9.1/python-programming-guide.html

# or [ Sat May 23 15:46:12 ~/Dev/spark-1.0.2-bin-hadoop2/bin ] ./pyspark
# ~/Dev/spark-1.0.2-bin-hadoop2/bin/pyspark
# words = sc.textFile("/usr/share/dict/words")
# words.filter(lambda w: w.startswith("spar")).take(5)

