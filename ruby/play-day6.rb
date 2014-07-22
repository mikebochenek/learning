# created 22.07.2014 20:31:19
# http://www.rubyinside.com/21-ruby-tricks-902.html

# 16 - Fight redundancy with Ruby's "logic" features
def is_odd(x)
  x % 2 == 0 ? false : true
end

def is_odd(x) # note that we can re-define the function without breaking anything...
  # Use the logical results provided to you by Ruby already..
  x % 2 != 0
end

class String
  def contains_digits?
    self[/\d/] ? true : false
  end
end

puts is_odd 3

s = String(3)
puts s.contains_digits? # note that function name can have question marks


# 17 - See the whole of an exception's backtrace

def do_division_by_zero; 5 / 0; end
begin
  do_division_by_zero
rescue => exception
  puts exception.backtrace
end