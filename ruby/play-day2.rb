# created 12.07.2014 23:04:30 
# http://stackoverflow.com/questions/tagged/ruby <-- higest voted ruby quetions

require 'securerandom'

class PlayDay2
  # http://stackoverflow.com/questions/948135/how-can-i-write-a-switch-statement-in-ruby
  def tryswitching(score)
    result = case score
    when 0..40 then "Fail"
    when 41..60 then "Pass"
    when 61..70 then "Pass with Merit"
    when 71..100 then "Pass with Distinction"
    else "Invalid Score"
    end
  end

end

# http://stackoverflow.com/questions/198460/how-to-get-a-random-number-in-ruby
puts(rand(10))
puts(rand(42-10) + 10)
puts(SecureRandom.random_number(100))

puts(PlayDay2.new.tryswitching(20))
# aha, so this is why ruby is popular, things just work as expected
