#!/usr/bin/ruby
require 'csv'
require 'mysql'

begin
  con = Mysql.new ARGV[0], ARGV[1], ARGV[2], ARGV[3]
  con.query('CREATE TABLE IF NOT EXISTS stations(id VARCHAR(5), name VARCHAR(40), eva_id INT(11)) '+
            'DEFAULT CHARACTER SET = utf8 ' +
            'COLLATE = utf8_bin'
            )
  stStm = con.prepare "INSERT INTO stations(id, name, eva_id) VALUES(?,?,?)"
  CSV.foreach("station.csv",{:col_sep => ";", :encoding=> "UTF-8:ISO-8859-1"}) do |row|
    stStm.execute row[0], row[1], row[2]
  end
rescue Mysql::Error => e
  puts e.errno
  puts e.error
  print trains2db.rb dbhost dbuser dbpass db
ensure
    con.close if con
end
