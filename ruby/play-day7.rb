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

