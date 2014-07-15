# created 15.07.2014 10:11:04
# http://www.rubyinside.com/21-ruby-tricks-902.html

# 1 - Extract regular expression matches quickly
x = 'this is a test'
puts x[/[aeiou].+?[aeiou]/] # => 'is i'

# 3 - Format decimal amounts quickly
money = 9.5
puts "%.2f" % money # => "9.50"
