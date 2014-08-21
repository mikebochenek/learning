# created 21.08.2014 21:25:01
# http://stackoverflow.com/questions/2167598/mysql-install-error-failed-to-build-gem-native-extension
#   mike-HP-Pavilion-dv8000-EE944AV / # sudo apt-get install libmysqlclient-dev
#   mike-HP-Pavilion-dv8000-EE944AV / # gem install mysql
# http://stackoverflow.com/questions/5795309/gem-install-mysql-fail
# http://zetcode.com/db/mysqlrubytutorial/
# http://rubylearning.com/satishtalim/ruby_mysql_tutorial.html

require "mysql"
require "mysql2"


sql = "select municipality, count(*) as cc
  FROM test.incomes 
  WHERE municipality <> 'MUNICIPALITY'
  group by municipality
  order by cc desc;"

m = Mysql.new("localhost", "test", "")
m.select_db('test')
rs = m.query(sql)

# this would simply print all rows (not rs.each vs. each_hash
# rs.each do |row|
#  puts row.join("\s") # print on one line
#end 
    
rs.each_hash do |row|
  # puts row.join("\s") # print on one line
  puts row['municipality']
end


# and now with mysql2
client = Mysql2::Client.new(
  :host => 'localhost', :database => 'test',
  :username => 'test')
res = client.query(sql, :as => :json)
res.each do |row|
  puts row
end 
