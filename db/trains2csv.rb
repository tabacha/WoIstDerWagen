require 'csv'
require 'nokogiri'


doc = File.open("BLS_oben.xml") { |f| Nokogiri::XML(f) }


sections = 'subtrains/subtrain/sections/identifier'
number = 'trainNumbers/trainNumber'
type = 'traintypes/traintype'
time = 'time'
addtext = 'additionalText'

station_id = doc.xpath("//shortcode").text

CSV.open("/tmp/file.csv", "wb", {col_sep: ';', quote_char: '"'}) do |csv|
  doc.xpath("//tracks/track/number").each do | track |
    doc.xpath("station/tracks/track[number=#{track.text}]/trains/train").each do |train|
    train_sections = train.xpath(sections).text
    train_number = train.xpath(number).first.text
    train_type = train.xpath(type).first.text
    train_time = train.xpath(time).text
    train_addtext = train.xpath(addtext).text.gsub("\n"," ")
    train_addtext.rstrip!
    csv << [ station_id, track.text, train_type, train_number, "#{train_type}#{train_number}", train_time, train_sections, train_addtext]
    end
  end
end
