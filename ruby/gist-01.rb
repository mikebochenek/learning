# created 22.07.2014 22:28:48
# somehow trying these ruby constructs is so enjoyable...

# https://gist.github.com/clayallsopp/1514595
3.times {
  puts "hello"
}

# https://gist.github.com/psalaets/5016914
puts "this is ruby #{RUBY_VERSION}-p#{RUBY_PATCHLEVEL}"

# https://gist.github.com/zenloner/5410836
1.upto(9) {|x| print x} #Prints "123456789"


# http://stackoverflow.com/questions/1020568/how-to-convert-a-string-to-lower-or-upper-case-in-ruby
puts "\n\nhello James!".upcase      #=> "HELLO JAMES!"
puts "hello James!".capitalize  #=> "Hello james!"
puts "hello James!".downcase! 
# If you want to modify a string in place, you can add an exclamation point to any of those methods:

# and you can find out all the methods available on a String by opening irb and running:
puts "MyString".methods.sort

# Find out 'case' methods:
puts "MyString".methods.grep(/case/)

# http://stackoverflow.com/questions/88311/how-best-to-generate-a-random-string-in-ruby
randomstring = (0...50).map { ('a'..'z').to_a[rand(26)] }.join
puts randomstring

# or even better...
require 'securerandom'
random_string = SecureRandom.hex
puts random_string