# created 17.07.2014 17:49:55
# http://www.rubyinside.com/21-ruby-tricks-902.html

# 6 - Exploding enumerables
a = %w{a b}
b = %w{c d}
[a + b]  # => [["a", "b", "c", "d"]]
[*a + b] # => ["a", "b", "c", "d"]

# 8 - Using non-strings or symbols as hash keys
does = is = { true => 'Yes', false => 'No' }
puts does[10 == 50]  # => "No"
puts is[10 > 5]     # => "Yes"

# 9 - Use 'and' and 'or' to group operations for single liners
# This is a trick that more confident Ruby developers use to tighten up their code
# and remove short multi-line if and unless statements:
queue = []
%w{hello x world}.each do |word|
  queue << word and puts "Added to queue" unless word.length <  2
end
puts queue.inspect

# 11 - Quick mass assignments
a, b, c, d = 1, 2, 3, 4  # thats not just ruby that allows this, right?
