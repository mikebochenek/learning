# created 21.08.2014 21:25:01
# http://stackoverflow.com/questions/2167598/mysql-install-error-failed-to-build-gem-native-extension
#   mike-HP-Pavilion-dv8000-EE944AV / # sudo apt-get install libmysqlclient-dev
#   mike-HP-Pavilion-dv8000-EE944AV / # gem install mysql
# http://stackoverflow.com/questions/5795309/gem-install-mysql-fail
# http://zetcode.com/db/mysqlrubytutorial/
# http://rubylearning.com/satishtalim/ruby_mysql_tutorial.html
# http://ruby.bastardsbook.com/chapters/sql/

require "mysql"
require "mysql2"
require "json"

def calc_score(city, year, m)

  sql1 = "SELECT sum(num_taxpayers) as total
    FROM test.incomes 
    where municipality like '" + city + "' and year = " + year + ";"
  rs = m.query(sql1)
  total_taxpayers = rs.fetch_row[0]

  # puts city + " " + year + " total_taxpayers: %.2f" % total_taxpayers.to_i


  sql2 = "SELECT income_group, sum(num_taxpayers) as total_count
    FROM test.incomes 
    where municipality like '" + city + "' and year = " + year + "
    group by income_group
    order by income_group asc;"
  rs = m.query(sql2)
  total_score = 0
  group_count_total = 0
  # puts JSON.generate({:city => city})
  rs.each_hash do |row|
    # puts row['income_group'] + '  ' + row['total_count']
    tc = row['total_count']
    ig = row['income_group'] 
    total_score += 1.0 * tc.to_i * ig.to_i / total_taxpayers.to_i
    group_count_total += tc.to_i
    # calculate and print MEDIAN GROUP... 
    # if (100 * group_count_total / total_taxpayers.to_i > 50) then puts ig end
    # puts JSON.generate({:ig => ig, :tc => tc})
  end
  total_score = total_score / 2
  puts city + "\t " + year + " total_score: \t%.2f" % total_score.to_s + "  [" + total_taxpayers + "]"
  # puts JSON.generate({:total_score => total_score})


  total_score
end

# calc_score('Zollikon', '2010', m)
# calc_score('Z%rich', '2010', m)
# calc_score('K%snacht', '2010', m)
# calc_score('Altikon', '2010', m)



sql = "select municipality, count(*) as cc
  FROM test.incomes 
  WHERE municipality <> 'MUNICIPALITY'
  group by municipality
  order by municipality asc;"

m = Mysql.new("localhost", "test", "")
m.select_db('test')
rs = m.query(sql)

# this would simply print all rows (not rs.each vs. each_hash
# rs.each do |row|
#  puts row.join("\s") # print on one line
#end 
    
rs.each_hash do |row|
  # puts row.join("\s") # print on one line
  # puts row['municipality']
  mun = row['municipality']
  calc_score(mun, '2010', m)
end


# and now with mysql2
client = Mysql2::Client.new(
  :host => 'localhost', :database => 'test',
  :username => 'test')
res = client.query(sql, :as => :json)
res.each do |row|
  # puts row
end 


thoughts = "here is what I am thinking, although I should probably think this through even more
create a .json file for each year
each file will contain a tree, with municipality as root
followed by additional information such as score etc. and individual values
home page could return a static .png file, until user clicks on it (and only then load interactive one)"



# so how do we calculate score?
# municipality with highest percentage of 45, 44, etc.
# Zollikon total is 7294, Zurich 233832

income_group_descriptions = "INCOME GROUP CODE;INCOME GROUP DESCRIPTION (CHF)
1;0-9999
2;10000-19999
3;20000-29999
4;30000-39999
5;40000-49999
6;50000-59999
7;60000-69999
8;70000-79999
9;80000-89999
10;90000-99999
11;100000-109999
12;110000-119999
13;120000-129999
14;130000-139999
15;140000-149999
16;150000-159999
17;160000-169999
18;170000-179999
19;180000-189999
20;190000-199999
21;200000-209999
22;210000-219999
23;220000-229999
24;230000-239999
25;240000-249999
26;250000-259999
27;260000-269999
28;270000-279999
29;280000-289999
30;290000-299999
31;300000-349999
32;350000-399999
33;400000-449999
34;450000-499999
35;500000-549999
36;550000-599999
37;600000-649999
38;650000-699999
39;700000-749999
40;750000-799999
41;800000-849999
42;850000-899999
43;900000-949999
44;950000-999999
45;1000000+
"
