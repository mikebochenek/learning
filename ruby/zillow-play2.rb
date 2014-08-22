# created 22.08.2014 21:12:35
# http://www.ruby-doc.org/stdlib-2.0.0/libdoc/json/rdoc/JSON.html

require 'json'

my_hash = {:hello => "goodbye"}
puts JSON.generate(my_hash) => "{\"hello\":\"goodbye\"}"

