# How to get data in to database
## Create a mysql database and a user

```mysql
CREATE DATABASE WoIstDerWagen
CREATE USER 'WoIstDerWagen'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON 'WoIstDerWagen' . * TO 'WoIstDerWagen'@'localhost';
FLUSH PRIVILEGES;
```

## Download data from OpenDataPortal and unzip it

```bash
wget http://download-data.deutschebahn.com/static/datasets/wagenstand/Wagenreihungsplan_RawData_20160617.zip
unzip Wagenreihungsplan_RawData_20160617.zip
```

## Import data to database

```bash
./stations2mysql.rb localhost WoIstDerWagen password WoIstDerWagen
./trains2mysql.rb localhost WoIstDerWagen password WoIstDerWagen
```

(Please not that it is not relay good that we transport the database password in the command line, so perhabs do this on your development machine and afterwards do a database dump and put it to your productional machine)

## TODO

Indexes and references on the database

## Weblinks

http://data.deutschebahn.com/dataset/data-wagenreihungsplan-soll-daten