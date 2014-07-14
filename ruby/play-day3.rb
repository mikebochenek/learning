# created 14.07.2014 22:54:52
# https://github.com/dreamr/beautiful-ruby-code

weekend = false
puts "go to office" unless weekend
# warning (...) interpreted as grouped expression play-day3.rb  /rubytest line 5  Problem

require 'date'
sunday = Date.today.strftime("%A") == "Sunday"
puts "check emails and do some coding" unless sunday


# good - Use the attr family of functions to define trivial accessors or mutators.
class Person
  attr_reader :first_name, :last_name

  def initialize(first_name, last_name)
    @first_name = first_name
    @last_name = last_name
  end
end

# better - Consider using Struct.new, which defines the trivial accessors, constructor and comparison operators for you.
class CompactPerson < Struct.new(:first_name, :last_name)
  
end



# good - Prefer literal array and hash creation notation (unless you need to pass parameters to their constructors, that is).
arr = []
hash = {}
