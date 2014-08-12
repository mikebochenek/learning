# created 10.08.2014 22:37:08
# http://stackoverflow.com/questions/16326008/accuracy-of-nanosecond-component-in-ruby-time
# and also see http://www.ruby-doc.org/core-2.1.2/Time.html

9.times do |count| 
  puts "try #{count} #{Time.now.nsec}"
end
