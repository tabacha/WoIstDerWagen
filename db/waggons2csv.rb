require 'csv'
require 'nokogiri'


doc = File.open("BL_tief.xml") { |f| Nokogiri::XML(f) }


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


station_id = doc.xpath("//shortcode").text

CSV.open("/tmp/file.csv", "wb", {col_sep: ';', quote_char: '"'}) do |csv|
  doc.xpath("//tracks/track/number").each do | track |
    doc.xpath("station/tracks/track[number=#{track.text}]/trains/train").each do |train|

    #train_sections = train.xpath(sections).text
    train_number = train.xpath(number).first.text
    train_type = train.xpath(type).first.text
    train_time = train.xpath(time).text
    train_addtext = train.xpath(addtext).text.gsub("\n"," ")
    train_addtext.rstrip!

      train.xpath(waggons).each do |waggon|
        waggon_position = waggon.xpath(waggonposition).text
        waggon_sections = waggon.xpath(waggonsections).text
        waggon_number = waggon.xpath(waggonnumber).text
        waggon_type = waggon.xpath(waggontype).text
        waggon_symbols = waggon.xpath(waggonsymbols).text


        csv << [ station_id, track.text, train_type, train_number, "#{train_type}#{train_number}", train_time, waggon_number, waggon_sections, train_addtext, waggon_position, waggon_type, waggon_symbols]
      end
    end
  end
end
