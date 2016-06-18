Station
-------

    +--------+-------------+------+-----+---------+-------+
    | Field  | Type        | Null | Key | Default | Extra |
    +--------+-------------+------+-----+---------+-------+
    | ID     | varchar(5)  | NO   | PRI |         |       |
    | Name   | varchar(40) | NO   |     | NULL    |       |
    | EVA_ID | int(11)     | NO   |     | NULL    |       |
    +--------+-------------+------+-----+---------+-------+

Trains
------

    +------------+--------------+------+-----+---------+-------+
    | Field      | Type         | Null | Key | Default | Extra |
    +------------+--------------+------+-----+---------+-------+
    | station_id | varchar(5)   | YES  |     | NULL    |       |
    | track_id   | varchar(4)   | YES  |     | NULL    |       |
    | type       | varchar(4)   | YES  |     | NULL    |       |
    | number     | int(11)      | YES  |     | NULL    |       |
    | name       | varchar(8)   | YES  |     | NULL    |       |
    | starttime  | time         | YES  |     | NULL    |       |
    | sections   | varchar(10)  | YES  |     | NULL    |       |
    | addtext    | varchar(256) | YES  |     | NULL    |       |
    +------------+--------------+------+-----+---------+-------+

Waggons
-------

    +----------------+--------------+------+-----+---------+-------+
    | Field          | Type         | Null | Key | Default | Extra |
    +----------------+--------------+------+-----+---------+-------+
    | station_id     | varchar(5)   | YES  |     | NULL    |       |
    | track_id       | varchar(4)   | YES  |     | NULL    |       |
    | traintype      | varchar(4)   | YES  |     | NULL    |       |
    | trainnumber    | int(11)      | YES  |     | NULL    |       |
    | trainname      | varchar(8)   | YES  |     | NULL    |       |
    | starttime      | time         | YES  |     | NULL    |       |
    | waggonname     | int(11)      | YES  |     | NULL    |       |
    | waggonsections | varchar(10)  | YES  |     | NULL    |       |
    | addtext        | varchar(256) | YES  |     | NULL    |       |
    | waggonposition | int(11)      | YES  |     | NULL    |       |
    | waggontype     | varchar(5)   | YES  |     | NULL    |       |
    | waggonsymbols  | varchar(10)  | YES  |     | NULL    |       |
    +----------------+--------------+------+-----+---------+-------+
