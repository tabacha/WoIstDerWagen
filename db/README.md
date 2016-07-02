# How to get data in to database
## Create a mysql database and a user

```mysql
CREATE DATABASE WoIstDerWagen
CREATE USER 'WoIstDerWagen'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `WoIstDerWagen` . * TO 'WoIstDerWagen'@'localhost';
FLUSH PRIVILEGES;
```


## Download data from OpenDataPortal and unzip it

```bash
wget http://download-data.deutschebahn.com/static/datasets/wagenstand/Wagenreihungsplan_RawData_20160617.zip
unzip Wagenreihungsplan_RawData_20160617.zip
```

## Import data to database

### Plain data import
```bash
./stations2mysql.rb localhost WoIstDerWagen password WoIstDerWagen
./trains2mysql.rb localhost WoIstDerWagen password WoIstDerWagen
```

This will create: 6560 stations, 14808 train and 172415 waggon entiers.

### Optional: Save the datatabse
```bash
mysqldump -uWoIstDerWagen -ppassword WoIstDerWagen >dump-raw.sql
```

### Prepare the data and remove uggly data.
```bash
mysql -uWoIstDerWagen -ppassword WoIstDerWagen <prepare_db.sql
```

After this step there will be 6560 stations, 13246 train and 153938 waggon entiers.


### Optional: Save the datatabse
```bash
mysqldump -uWoIstDerWagen -ppassword WoIstDerWagen >dump-work.sql
```


(Please not that it is not relay good that we transport the database password in the command line, so perhabs do this on your development machine and afterwards do a database dump and put it to your productional machine)

## Weblinks

http://data.deutschebahn.com/dataset/data-wagenreihungsplan-soll-daten