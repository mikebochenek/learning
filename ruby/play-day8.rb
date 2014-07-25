# created 24.07.2014 20:23:13

puts "the great battle of nil vs. empty"

puts nil.nil?
puts false.nil?
puts [].nil?.to_s + " vs. " + [].empty?.to_s
puts {}.nil? # ... strangely we don't print anything here
puts "".nil?.to_s + " vs. " + "".empty?.to_s
puts 5.nil?


puts
puts "checking if a variable is defined or not"
a = 1
puts defined? a
puts defined? b
puts defined? String
puts defined? 1

