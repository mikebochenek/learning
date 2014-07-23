# created 23.07.2014 22:23:54
# now for something completely different and completely original:
# a factorial function with unit tests
# http://en.wikibooks.org/wiki/Ruby_Programming/Syntax/Method_Calls

def factorial(x) 
  x <= 2 ? x : x * factorial(x - 1)
end

# http://en.wikibooks.org/wiki/Ruby_Programming/Unit_testing
require "test/unit"

class TestSimpleNumber < Test::Unit::TestCase
  def test_simple
    assert_equal(0, factorial(0))
    assert_equal(1, factorial(1))
    assert_equal(5040, factorial(7))
    assert_equal(3628800, factorial(10))
  end
end


# page 164 of Discrete Mathematics and Its Applications by Kenneth H. Rosen
# question #6. Given a positive integer, determine whether it is prime.
def is_prime(i)
  return false if i <= 1
  2.upto(Math.sqrt(i).to_i) do |x|
    return false if i % x == 0
  end
  true
end

puts "19 should be prime: " + is_prime(19).to_s
puts "23244 shoult not be prime: " + is_prime(23244).to_s # 23244 = 2 x 2 x 3 x 13 x 149 

# but wait, there is more, ruby actually has this built in... 
require 'prime'

Prime.take(10) #=> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Prime.take_while {|p| p < 10 } #=> [2, 3, 5, 7]
puts Prime.prime?(19) #=> true
