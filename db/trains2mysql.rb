#!/usr/bin/ruby
require 'csv'
require 'nokogiri'
require 'mysql'

directory = 'Wagenreihungsplan_RawData_20160617/'
sections = 'subtrains/subtrain/sections/identifier'
number = 'trainNumbers/trainNumber'
type = 'traintypes/traintype'
time = 'time'
addtext = 'additionalText'
waggons = 'waggons/waggon'

waggonposition = 'position'
waggonsections = 'sections/identifier'
waggonnumber = 'number'
waggontype = 'type'
waggonsymbols = 'symbols'


begin
  con = Mysql.new ARGV[0], ARGV[1], ARGV[2], ARGV[3]
  con.query('CREATE TABLE IF NOT EXISTS stations(id VARCHAR(5), name VARCHAR(40), eva_id INT(11))')
  con.query('CREATE TABLE IF NOT EXISTS trains(id int(6), station_id VARCHAR(5), track_id VARCHAR(5), track_name VARCHAR(15), type VARCHAR(4), number int(11), starttime time, sections VARCHAR(10), additional_text VARCHAR(256))')
  con.query('CREATE TABLE IF NOT EXISTS waggons(train_id int(6), number int(11), sections varchar(11), position int(2), type VARCHAR(5), symbols VARCHAR(10))')
  trainStm = con.prepare "INSERT INTO trains(id, station_id,  track_id, track_name, type, number, starttime, sections, additional_text) VALUES(?,?,?,?,?,?,?,?,?)"
  wgnStm = con.prepare "INSERT INTO waggons(train_id, number, sections, position, type, symbols) VALUES(?,?,?,?,?,?)"
  files= Dir.entries(directory)
  index=0
  files.each do | file |
    if (file =~ /\.xml2/) 
      print directory+file,"\n";
      doc = File.open(directory+file) { |f| Nokogiri::XML(f) }
      station_id = doc.xpath("//shortcode").text
      print station_id,"\n"
    end
    if (file =~ /\.xml/) 
      doc = File.open(directory+file) { |f| Nokogiri::XML(f) }
      station_id = doc.xpath("//shortcode").text
      doc.xpath("//tracks/track").each do | track |
        track.xpath("trains/train").each do |train|
          begin
            train_sections = train.xpath(sections).text
            train_number = train.xpath(number).first.text
            train_type = train.xpath(type).first.text
            train_time = train.xpath(time).text
            train_addtext = train.xpath(addtext).text.gsub("\n"," ")
            train_addtext.rstrip!
            index = index + 1
            
            train.xpath(waggons).each do |waggon|
              waggon_position = waggon.xpath(waggonposition).text
              waggon_sections = waggon.xpath(waggonsections).text
              waggon_number = waggon.xpath(waggonnumber).text
              waggon_type = waggon.xpath(waggontype).text
              waggon_symbols = waggon.xpath(waggonsymbols).text
  
              wgnStm.execute index, waggon_number, waggon_sections, waggon_position, waggon_type, waggon_symbols
            end

            trainStm.execute index, station_id, track.xpath('number').text, track.xpath('name').text, train_type, train_number, train_time, train_sections, train_addtext
          rescue Mysql::Error
            #reraise the same exeception
            raise
          rescue Exception => e  
            print file, ' Line: ', train.line, ' ', e, "\n"
          end
        end
      end
    end
  end
rescue Mysql::Error => e
  puts e.errno
  puts e.error
  print "trains2db.rb dbhost dbuser dbpass db"
ensure
    con.close if con
end
